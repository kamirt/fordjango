# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext as _



class UserRegForm(forms.Form):
    email = forms.CharField(label=_(u'E-mail'), widget=forms.EmailInput(attrs = {"class":"input_text"}))
    password = forms.CharField(label=_(u'Password'), widget=forms.PasswordInput(attrs = {"class":"input_text"}))
    password_confirm = forms.CharField(label=_(u'Пароль еще раз'), widget=forms.PasswordInput(attrs = {"class":"input_text"}))


class SendEmailForm(forms.Form):
    text = forms.CharField(required = True, widget=forms.Textarea(attrs = {"class":"input_textarea"}))
    email= forms.CharField(required = True, widget=forms.TextInput(attrs = {"class":"input_text"}))
    name = forms.CharField(widget=forms.TextInput(attrs = {"class":"input_text"}))

class SubscribeForm(forms.Form):
	subname= forms.CharField(required=True, widget=forms.TextInput(attrs = {"class":"subscribeinput","placeholder":"Имя"}))
	subemail = forms.CharField(required=True,widget=forms.EmailInput(attrs = {"class":"subscribeinput","placeholder":"e-mail"}))
	subphone = forms.CharField(required=False,widget=forms.TextInput(attrs = {"class":"subscribeinput","id":"phone","placeholder":"Телефон"}))
	subskype = forms.CharField(required=False,widget=forms.TextInput(attrs = {"class":"subscribeinput","placeholder":"Skype"}))
	subhid = forms.CharField(required=True, widget=forms.HiddenInput(attrs = {"value":"subscr"}))
	
                                
