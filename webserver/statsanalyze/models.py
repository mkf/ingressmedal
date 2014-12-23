from django.db import models
from django.utils import timezone

# Create your models here.

class Entry(models.Model):
	agentdb = models.ForeignKey('Agent')
	creator = models.ForeignKey('auth.User')
	owner = models.ForeignKey('auth.User')
	public = models.BooleanField()
	ocreddirectly = models.BooleanField()
	idnumber = models.CharField(max_length=50) # unix time + 10 random characters
	codename = models.CharField(max_length=50)
	entry_date = models.DateTimeField('Entry datetime')
	added_time = models.DateTimeField(default=timezone.now)
	parama = models.PositiveIntegerField()
	paramb = models.PositiveIntegerField()
	paramc = models.PositiveIntegerField()

	def addentry(self):
		self.added_time = timezone.now()
		self.save()

	def __str__(self):
		return str(self.codename)+" "+str(self.idnumber)

#class Stat(models.Model):
#
#class Agent(models.Model):
#
#class User(models.Model):
#