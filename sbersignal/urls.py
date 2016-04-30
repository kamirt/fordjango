from django.conf.urls import patterns, include, url
from django.contrib import admin
from sbersignal import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login,logout


urlpatterns = [
	url(r'^$', views.main, name='home'),
	url(r'^buy/$', views.buy, name='buy'),
	url(r'^contacts/$', views.contacts, name='contacts'),
	url(r'^registration/$', views.registration_view, name='registration'),
	url(r'^login/$', views.login),
	url(r'^stat/$', views.statistic),
]
