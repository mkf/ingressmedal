# -*- coding: utf-8 -*-
__author__ = 'ArchieT'
from django.conf.urls import patterns,include,url
from . import views

urlpatterns = patterns(
	'',
	url(r'^$',views.glowna),
	url(r'^$',views.agents_list()),
	url(r'^login.html$',views.login),
	url(r'^login_error.html$',views.login_error),
#	url('', include('social.apps.django_app.urls', namespace='social')),
#	url('', include('django.contrib.auth.urls', namespace='auth')),
	url(r'',include('social_auth.urls')),
)