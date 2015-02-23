from django.db import models
from django.utils import timezone

# Create your models here.

class Entry(models.Model):
	alltime = 'AllTime'
	month = 'Month'
	week = 'Week'
	timepartchoices = (
		(alltime,'AllTime'),
		(month,'Month'),
		(week,'Week'),
	)
	timepart = models.CharField(max_length=7,choices=timepartchoices,default=alltime)
	agentdb = models.ForeignKey('Agent')
	creator = models.ForeignKey('User',related_name='entrycreator')
	owner = models.ForeignKey('User',related_name='entryowner')
	public = models.BooleanField()
	ocreddirectly = models.BooleanField()
	idnumber = models.CharField(max_length=50) # unix time + 10 random characters
	entry_date = models.DateTimeField('Entry datetime')
	added_time = models.DateTimeField(default=timezone.now())
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
#	guardnow = models.PositiveIntegerField(blank=True)
	guardlink = models.PositiveIntegerField()
	maxlinklenxdays = models.PositiveIntegerField()
	guardfield = models.PositiveIntegerField()
	maxfieldmuxdays = models.PositiveIntegerField()
	hack = models.PositiveIntegerField()
	uniqmis = models.PositiveIntegerField()
	glyph = models.PositiveIntegerField()
	edits = models.PositiveIntegerField(blank=True,null=True)
	photos = models.PositiveIntegerField(blank=True,null=True)
	recruiter = models.PositiveIntegerField(blank=True,null=True)

	def __str__(self):
		return str(self.agentdb.codename)+" "+str(self.idnumber)

class NowEntry(models.Model):
	agentdb = models.ForeignKey('Agent')
	creator = models.ForeignKey('User',related_name='nowentrycreator')
	owner = models.ForeignKey('User',related_name='nowentryowner')
	public = models.BooleanField()
	ocreddirectly = models.BooleanField()
	idnumber = models.CharField(max_length=50) # unix time + 10 random characters
	entry_date = models.DateTimeField('Entry datetime')
	added_time = models.DateTimeField(default=timezone.now())
	ap = models.PositiveIntegerField()
	bronze = models.PositiveIntegerField()
	silver = models.PositiveIntegerField()
	gold = models.PositiveIntegerField()
	platinum = models.PositiveIntegerField()
	onyx = models.PositiveIntegerField()
	nomedal = models.PositiveIntegerField()
	linksactiv = models.PositiveIntegerField()
	fieldsactiv = models.PositiveIntegerField()
	pwned = models.PositiveIntegerField()
	mucontrol = models.PositiveIntegerField()

	def __str__(self):
		return str(self.agentdb.codename)+" "+str(self.idnumber)

class Agent(models.Model):
	codename = models.CharField(max_length=30,unique=True)
	created = models.DateTimeField()
	modified = models.DateTimeField()
	dbowner = models.ForeignKey('User',related_name='agentdbowner')
	creator = models.ForeignKey('User',related_name='agentcreator')
	public = models.BooleanField()
	knownemailone = models.EmailField(blank=True)
	knownemailtwo = models.EmailField(blank=True)
	knownemailthree = models.EmailField(blank=True)
	googleplusurlone = models.URLField(blank=True)
	googleplusurltwo = models.URLField(blank=True)
	googleplusurlthree = models.URLField(blank=True)
	otherurlone = models.URLField(blank=True)
	otherurltwo = models.URLField(blank=True)
	otherurlthree = models.URLField(blank=True)
	notes = models.TextField(blank=True)

	def __str__(self):
		return str(self.codename)

class User(models.Model):
	personality = models.ForeignKey('auth.User')
	owncodename = models.CharField(max_length=30, blank=True, null=True)

	def __str__(self):
		return str(self.personality)