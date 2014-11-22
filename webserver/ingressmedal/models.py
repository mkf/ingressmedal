# -*- coding: utf-8 -*-

from django.db import models

class agentsdata(models.Model):
	codename = models.CharField(max_length=30,unique=True)
	created = models.DateTimeField()
	modified = models.DateTimeField()