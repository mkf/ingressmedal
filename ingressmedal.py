#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import argparse
interactively = 'This will disappear from here soon, and remember about that else for interactively below'
class current:
	"This class applies only to current stats, it doesn't compare anything to the past"
	def __init__(self,codename,interactively):
		from interactive import *
		interaktywnosc = interactive()
		self.interaktywnosc = interaktywnosc
		if interactively == True:
			print "Input for agent %s" % codename
			self.current = interaktywnosc.current()
		elif interactively == False:
			print "It can't be False yet."
		else:
			for kluczykowo in interaktywnosc.gimmecurrentquestionsuredict().keys():
				try:
					bzdurkaldkfh = str(self.current[kluczykowo])
				except:
					self.current[kluczykowo] = interaktywnosc.currentwyrywki(kluczykowo)
			for kluczykowo in interaktywnosc.gimmecurrentquestionunsuredict().keys():
				try:
					bzdurkafdhgljsdk = str(self.current[kluczykowo])
				except:
					self.current[kluczykowo] = interaktywnosc.currentwyrywki(kluczykowo)
	def rjeturncount(self):
		return self.current
	def coUNTINGcurapcountable(self):
			current = self.current
			curapcountable = {
				'seer': (current['seer']*1000),
				'depllater': ((current['depl']-current['capt'])*125),
				'link': (current['link']*313),
				'field': (current['field']*1250),
				'rechmin': (current['rech']*10),
				'captres': (current['capt']*625),
				'destr': (current['destr']*75),
				'destrlink': (current['destrlink']*187),
				'destrfield': (current['destrfield']*750),
			}
			if current['photo'] == 'n':
				print "That's your fault you don't know how much AP you've gained on photos."
			else:
				curapcountable['photo'] = (current['photo']*500)
			if current['edit'] == 'n':
				print "That's your fault you don't know how much AP you've gained on edits."
			else:
				curapcountable['edit'] = (current['edit']*200)
			return curapcountable
	def percent(self):
			things = self.coUNTINGcurapcountable()
			for w in sorted(things, key=things.get, reverse=True):
				print w, things[w]


hello = current('ArchieT', interactively)
hello.coUNTINGcurapcountable()