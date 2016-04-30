# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin

import hashlib, datetime, random
from django.utils import timezone
from sbersignal.celery import first_mail_task

#News, for right up module of page, not understand, what it is
class News(models.Model):
	news_header = models.CharField(max_length=100, verbose_name="Заголовок новости")
	news_body = models.CharField(max_length=200, verbose_name="Новость")
	public_date = models.DateField(auto_now_add=False, verbose_name="Дата_создания")
	class Meta:
		verbose_name = u'Новость'
		verbose_name_plural = u'Новости'




#this used for placing some "past results". Have no any idea, from where he get them
class PastResults(models.Model):
	first_number = models.PositiveIntegerField()
	second_number = models.PositiveIntegerField()
	public_date = models.DateField(auto_now_add=False, verbose_name="Дата")
	class Meta:
		verbose_name = u'Предыдущий результат'
		verbose_name_plural = u'Предыдущие результаты'
#"main" class. For the recommendations in the left up corner. 
class Recommendation(models.Model):
	date_of_rec = models.DateTimeField(auto_now_add=False, verbose_name="C")
	date_of_rec_ex = models.DateTimeField(auto_now_add=False, verbose_name="По")
	rec_choices = (
		('buy', "Покупка"),
		('sell', "Продажа")
		)
	rec = models.CharField(max_length=100, choices = rec_choices, default='buy', verbose_name="Сигнал")

	def __unicode__(self):
		return u'c %s по %s' % (self.date_of_rec.date, self.date_of_rec_ex.date)

	def __str__(self):
		return u'c %s по %s' % (self.date_of_rec, self.date_of_rec_ex)

	class Meta:
		verbose_name = u'Сигнал'
		verbose_name_plural = u'Сигналы'
#this for the convenient view in the admin panel
class RecommendationAdmin(admin.ModelAdmin):
	list_display = ('date_of_rec', 'date_of_rec_ex', 'rec')
	list_display_links = ('date_of_rec', 'date_of_rec_ex')
#subscribing form save units in this model
class Subscribers(models.Model):
	name = models.CharField(max_length=50)
	phone = models.CharField(max_length=17)
	email = models.CharField(max_length=100)
	skype = models.CharField(max_length=100)
	def __unicode__(self):
		return u'%s, %s' % (self.name, self.email)

	class Meta:
		verbose_name = u'Профиль'
		verbose_name_plural = u'Подписчики'
#first letter sending to the new subscriber
class FirstLetter(models.Model):
	subject = models.CharField(max_length=200)
	text = models.TextField()
	class Meta:
		verbose_name = u'Первое_письмо'
		verbose_name_plural = u'Первые_письма'
#this for responding. 
class Emails(models.Model):
	subject = models.CharField(max_length=200)
	text = models.TextField()
	class Meta:
		verbose_name = u'Рассылка'
		verbose_name_plural = u'Рассылки'
	def __str__(self):
		return u'%s' % (self.subject)
"""its not the right way maybe, but this method sends letter any time it has been created and saved.
Client creates a letter, template is injected, and as he click on "save", this letter sending to all
subscribers""" 
	def save(self, *args, **kwargs):
		email = Subscribers.objects.all()
		addresses = []
		for i in email:
			addresses.append(i.email)
		print (addresses)
		subject = self.subject
		context = self.text
		super(Emails, self).save(*args, **kwargs)
		first_mail_task.delay(email=addresses, subject=subject, context=context)

