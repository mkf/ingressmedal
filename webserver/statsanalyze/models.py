from django.db import models

# Create your models here.

class Entry(models.Model):
	entrdate = models.DateTimeField('Entry date')

#class Stat(models.Model):
#
#class Agent(models.Model):
#
#class User(models.Model):
#