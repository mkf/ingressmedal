from django.db import models
from django.utils import timezone

# Create your models here.

class Entry(models.Model):
	agentdb = models.ForeignKey('Agent')
	creator = models.ForeignKey('User',related_name='entrycreator')
	owner = models.ForeignKey('User',related_name='entryowner')
	public = models.BooleanField()
	ocreddirectly = models.BooleanField()
	idnumber = models.CharField(max_length=50) # unix time + 10 random characters
	codename = models.CharField(max_length=50)
	entry_date = models.DateTimeField('Entry datetime')
	added_time = models.DateTimeField(blank=True,null=True)
	ap = models.PositiveIntegerField()
	bronze = models.PositiveIntegerField()
	silver = models.PositiveIntegerField()
	gold = models.PositiveIntegerField()
	platinum = models.PositiveIntegerField()
	onyx = models.PositiveIntegerField()
	nomedal = models.PositiveIntegerField()
	uniqvis = models.PositiveIntegerField()
	seer = models.PositiveIntegerField()
	xm = models.PositiveIntegerField()
	walk = models.PositiveIntegerField()
	depl = models.PositiveIntegerField()
	link = models.PositiveIntegerField()
	field = models.PositiveIntegerField()
	allfieldmusum = models.PositiveIntegerField()
	longestlink = models.PositiveIntegerField()
	largestfield = models.PositiveIntegerField()
	rech = models.PositiveIntegerField()
	capt = models.PositiveIntegerField()
	uniqcapt = models.PositiveIntegerField()
	mods = models.PositiveIntegerField()
	destr = models.PositiveIntegerField()
	neutr = models.PositiveIntegerField()
	destrlink = models.PositiveIntegerField()
	destrfield = models.PositiveIntegerField()
	guard = models.PositiveIntegerField()
	guardnow = models.PositiveIntegerField()
	guardlink = models.PositiveIntegerField()
	maxlinklenxdays = models.PositiveIntegerField()
	guardfield = models.PositiveIntegerField()
	maxfieldmuxdays = models.PositiveIntegerField()
	hack = models.PositiveIntegerField()
	edits = models.PositiveIntegerField()
	photos = models.PositiveIntegerField()

	def addentry(self):
		self.added_time = timezone.now()
		self.save()

	def __str__(self):
		return str(self.codename)+" "+str(self.idnumber)


class Agent(models.Model):
	codename = models.CharField(max_length=50)
	dbowner = models.ForeignKey('User',related_name='agentdbowner')
	creator = models.ForeignKey('User',related_name='agentcreator')
	public = models.BooleanField()
	knownemailone = models.EmailField()
	knownemailtwo = models.EmailField()
	knownemailthree = models.EmailField()
	googleplusurlone = models.URLField()
	googleplusurltwo = models.URLField()
	googleplusurlthree = models.URLField()
	otherurlone = models.URLField()
	otherurltwo = models.URLField()
	otherurlthree = models.URLField()
	notes = models.TextField()

class User(models.Model):
	personality = models.ForeignKey('auth.User')