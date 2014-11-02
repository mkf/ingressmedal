#!/usr/bin/python2
# -*- coding: utf-8 -*-

class current:
	"This class applies only to current stats, it doen't compare anything to the past"
	def __init__(self,codename):
		print "Input for agent %s" % codename
		current = {}
		isint = False
		while isint == False:
			try:
				current['ap'] = int(raw_input('Current AP: '))
			except ValueError:
				print "Value is not int"
				isint = False
		isint = False
		while isint == False:
			try:
				current['uniqvis'] = int(raw_input('Current count of unique portals visited: '))
			except ValueError:
				print "Value is not int"
				isint = False
		isint = False
		while isint == False:
			try:
				current['seer'] = int(raw_input('Current count of discovered portals: '))
			except ValueError:
				print "Value is not int"
				isint = False
		isint = False
		while isint == False:
			try:
				current['hack'] = int(raw_input('Current count of hacks: '))
			except ValueError:
				print "Value is not int"
				isint = False
		isint = False
		while isint == False:
			try:
				current['depl'] = int(raw_input('Current count of deployed resonators: '))
			except ValueError:
				print "Value is not int"
				isint = False
		isint = False
		while isint == False:
			try:
				current['link'] = int(raw_input('Current count of created links: '))
			except ValueError:
				print "Value is not int"
				isint = False
		isint = False
		while isint == False:
			try:
				current['field'] = int(raw_input('Current count of created Control Fields: '))
			except ValueError:
				print "Value is not int"
				isint = False
		isint = False
		while isint == False:
			try:
				current['rech'] = int(raw_input('Current count of recharged XM: '))
			except ValueError:
				print "Value is not int"
				isint = False
		isint = False
		while isint == False:
			try:
				current['capt'] = int(raw_input('Current count of captured portals: '))
			except ValueError:
				print "Value is not int"
				isint = False
		isint = False
		while isint == False:
			try:
				current['uniqcapt'] = int(raw_input('Current count of unique portals captured: '))
			except ValueError:
				print "Value is not int"
				isint = False
		isint = False
		while isint == False:
			try:
				current['destr'] = int(raw_input('Current count of destroyed resonators: '))
			except ValueError:
				print "Value is not int"
				isint = False
		isint = False
		while isint == False:
			try:
				current['guard'] = int(raw_input('Current max time portal held in days: '))
			except ValueError:
				print "Value is not int"
				isint = False
		isint = False
		while isint == False:
			try:
				current['destrlink'] = int(raw_input('Current count of enemy links destroyed: '))
			except ValueError:
				print "Value is not int"
				isint = False
		isint = False
		while isint == False:
			try:
				current['destrfield'] = int(raw_input('Current count of enemy Control Fields destroyed: '))
			except ValueError:
				print "Value is not int"
				isint = False
		isintorn = False
		while isintorn == False:
			phototry = raw_input("Current count of photos approved to portals (check mail) (number (even if it's 0) or 'n' character if you don't know): ")
			try:
				current['photo'] = int(phototry)
			except ValueError:
				print "Value is not int"
				if phototry == "n":
					current['photo'] = 'n'
					print "So you don't know, huh?"
				else:
					print "It is neither a number nor 'n', you seriously don't know how to answer such a simple question??"
					isintorn = False
		while isintorn == False:
			phototry = raw_input("Current count of photos approved to portals (check mail) (number (even if it's 0) or 'n' character if you don't know): ")
			try:
				current['edit'] = int(phototry)
			except ValueError:
				print "Value is not int"
				if phototry == "n":
					current['edit'] = 'n'
					print "So you don't know, huh?"
				else:
					print "It is neither a number nor 'n', you seriously don't know how to answer such a simple question??"
					isintorn = False
		self.current = current
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