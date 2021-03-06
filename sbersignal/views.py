# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from sbersignal.forms import UserRegForm, SendEmailForm, SubscribeForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse
from django.core.context_processors import csrf
from sbersignal.models import *
from django.core.mail import send_mail
from datetime import datetime, date, time
from django.utils import timezone
from sbersignal.celery import first_mail_task
from dateutil.relativedelta import *
from django.template.loader import get_template
from django.template import Context, Template
from django.core.mail import EmailMultiAlternatives
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#this on each page, execept "buy", so this function have no its own url. Works on subscribe form
def subscribtion(rp):
	hidrequest = rp['subhid']
	subname = rp['subname']
	subemail = rp['subemail']
	subphone = rp['subphone']
	subskype = rp['subskype']
	subhid = rp['subhid']
	newsubscriber = Subscribers.objects.create(name=subname, email=subemail, phone=subphone, skype=subskype)
	newsubscriber.save()
	frommodelsubject = FirstLetter.objects.all().order_by("subject", "text")[:1]
	for i in frommodelsubject:
		subject=i.subject
		context = i.text
	email = [subemail]
	first_mail_task(email=email, subject=subject, context=context)	
	return redirect("/sbersignal")

#as well as content is almost indentity, other functions also uses this, like above.
def context_return():
	news = News.objects.all().order_by("-public_date")[:3]
	pastres = PastResults.objects.all().order_by("-public_date")[:4]
	rec = Recommendation.objects.all().order_by("-date_of_rec_ex")[:4]
	context = { 'news':news, 'pastres':pastres, 'rec':rec }
	return context
#this function using by "main" function for cut the content for unregistered users
def cutted_context():
	news = News.objects.all().order_by("-public_date")[:3]
	pastres = PastResults.objects.all().order_by("-public_date")[:4]
	rec = Recommendation.objects.all().order_by("-date_of_rec_ex")[:4]
	rec1 = rec[1]
	rec2 = rec[2]
	rec3 = rec[3]
	context = { 'news':news, 'pastres':pastres, 'rec1':rec1, 'rec2':rec2, 'rec3':rec3 }
	return context
# function for the homepage. Attention on context. It depends on status of user.
def main (request):
	#for "privileged" users we show all information
	if request.user.is_authenticated and request.user.is_active:
		context = context_return()
		subform = SubscribeForm(request.POST or None)
		context['subform'] = subform
		if request.method == 'POST' and subform.is_valid():
			rp = request.POST
			subscribtion(rp)
		return render(request, 'index.html', context)
	else:
		#for new users or it they inactive(unpayed) we check out the time
		# let's compare some dates with other certain hours and minutes
		nowdate = datetime.now()
		td = datetime.weekday(nowdate)
		print(nowdate)
		comparetime_one = nowdate+relativedelta(hour=10)
		comparetime_two = nowdate+relativedelta(hour=11, minute=30)
		comparetime_three = nowdate+relativedelta(hour=14)
		comparetime_four = nowdate+relativedelta(hour=15, minute=30)
		#if time is between 10.00am and 11.30am and today is not a weekend
		#show only three past recommendations, and the remaining time
		if nowdate>=comparetime_one and nowdate<=comparetime_two and td!=5 and td!=6:
			context = cutted_context()
			subform = SubscribeForm(request.POST or None)
			context['subform'] = subform
			counter = comparetime_two-nowdate
			context['counter'] = str(counter)[2:4]
			context['counter2'] = str(counter)[0:1]
		#dont forget about subscribtion form
			if request.method == 'POST' and subform.is_valid():
				rp = request.POST
				subscribtion(rp)
			return render(request, 'indexp.html', context)
		#if time is between other interval, also must not be a weekend
		elif nowdate>=comparetime_three and nowdate<=comparetime_four and td!=5 and td!=6:
			context = cutted_context()
			subform = SubscribeForm(request.POST or None)
			context['subform'] = subform
			counter = comparetime_four-nowdate
			context['counter'] = str(counter)[2:4]
			context['counter2'] = str(counter)[0:1]
		#of course, subscribtion form
			if request.method == 'POST' and subform.is_valid():
				rp = request.POST
				subscribtion(rp)
			return render(request, 'indexp.html', context)
		#in the rest of time, show all the information, as if the user is active
		else:
			context = context_return()
			subform = SubscribeForm(request.POST or None)
			context['subform'] = subform
			if request.method == 'POST' and subform.is_valid():
				rp = request.POST
				subscribtion(rp)
			return render(request, 'index.html', context)

		

	

def statistic(request):
	news = News.objects.all().order_by("-public_date")[:3]
	rec = Recommendation.objects.all().order_by("-date_of_rec_ex")[:4]
	pages = PastResults.objects.all().order_by("-public_date")
	
	pastres = PastResults.objects.all().order_by("-public_date")[:4]
	paginator = Paginator(pages, 8) # Show 8 results on one page
	i=[]
	count=1
	for pg in range(len(pages)):
		i.append(count)
		count = count+1

	page = request.GET.get('page')
	try:
		listpage = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		listpage = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		listpage = paginator.page(paginator.num_pages)
	context = { 'news':news, 'listpage':listpage, 'rec':rec, 'pastres':pastres, 'nums': i }

	subform = SubscribeForm(request.POST or None)
	context['subform'] = subform
	if request.method == 'POST' and subform.is_valid():
		rp = request.POST
		subname = rp['subname']
		subemail = rp['subemail']
		subphone = rp['subphone']
		subskype = rp['subskype']
		subhid = rp['subhid']
		newsubscriber = Subscribers.objects.create(name=subname, email=subemail, phone=subphone, skype=subskype)
		newsubscriber.save()
		frommodelsubject = FirstLetter.objects.all().order_by("subject", "text")[:1]
		for i in frommodelsubject:
			subject=i.subject
			context = i.text
		email = [subemail]
		first_mail_task(email=email, subject=subject, context=context)
		text = {'context':subject}
		return redirect("/sbersignal")
	return render(request, 'statistics.html', context)

def buy (request):
    return render(request, 'buy.html')

def contacts (request):
	context = context_return()
	form = SendEmailForm(request.POST or None)
	subform = SubscribeForm(request.POST or None)
	context['subform'] = subform
	context['formcontact'] = form
	if request.method == 'POST':
		rp = request.POST
		try:
			subscribtion(rp)
		except:
			message = rp['text']
			email = rp['email']
			name = rp['name']
			send_mail('От ' + email + ', ' + name, message, 'kamirt@yandex.ru', ['kamirt@yandex.ru'], fail_silently=False)
			return HttpResponse('Ваше сообщение успешно отправлено!')

	return render(request, 'contacts.html', context)

def login(request):
	context = context_return()
	subform = SubscribeForm(request.POST or None)
	context['subform'] = subform
	if request.method == 'POST':
		rp = request.POST
		subscribtion(rp)
	return render(request, 'sberlogin.html', context)

def registration_view(request):
	context = context_return()
	form = UserRegForm(request.POST or None)
	context['form'] = form
	subform = SubscribeForm(request.POST or None)
	context['subform'] = subform
	if request.method == 'POST':
		rp = request.POST
		try:
			subscribtion(rp)
		except:
			password = form.cleaned_data.get('password', None)
			password_confirm = form.cleaned_data.get('password_confirm', None)
			email = form.cleaned_data.get('email', None)
			username = email
			if password==password_confirm:
				user = User.objects.create_user(username, email, password)
				user.save()
				user = auth.authenticate(username=username, password=password)
				if user.is_authenticated():
					auth.login(request, user)
					return redirect('/sbersignal')
			else: 
				return HttpResponse("Пароли не совпадают <a href='/registration/'>Попробовать еще раз</a>")
	return render(request, 'registration.html', context)

