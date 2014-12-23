# -*- coding: utf-8 -*-
__author__ = 'ArchieT'
from django.conf.urls import patterns,include,url
from . import views

urlpatterns = patterns(
	'',
	url(r'^$',views.agents_list)
)