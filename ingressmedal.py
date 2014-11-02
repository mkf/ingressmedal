#!/usr/bin/python2
# -*- coding: utf-8 -*-

class agent:
	"Klasa dotycząca pojedyńczego agenta"
	def __init__(self,codename):
		print "Input for agent %s" % codename
		isint = False
		while isint == False:
			try:
				cap = int(raw_input('Current AP: '))
			except ValueError:
				print "Value is not int"
				isint = False
		isint = False
		while isint == False:
			try:
				cuniqvis = int(raw_input('Current count of unique portals visited: '))
			except ValueError:
				print "Value is not int"
				isint = False
		isint = False
		while isint == False:
			try:
				cseer = int(raw_input('Current count of discovered portals: '))
			except ValueError:
				print "Value is not int"
				isint = False
		isint = False
		while isint == False:
			try:
				chack = int(raw_input('Current count of hacks: '))
			except ValueError:
				print "Value is not int"
				isint = False
		isint = False
		while isint == False:
			try:
				cdepl = int(raw_input('Current count of deployed resonators: '))
			except ValueError:
				print "Value is not int"
				isint = False
		isint = False
		while isint == False:
			try:
				clink = int(raw_input('Current count of created links: '))
			except ValueError:
				print "Value is not int"
				isint = False
		isint = False
		while isint == False:
			try:
				cfields = int(raw_input('Current count of created Control Fields: '))
			except ValueError:
				print "Value is not int"
				isint = False
		isint = False
		while isint == False:
			try:
				crech = int(raw_input('Current count of recharged XM: '))
			except ValueError:
				print "Value is not int"
				isint = False
		isint = False
		while isint == False:
			try:
				ccapt = int(raw_input('Current count of captured portals: '))
			except ValueError:
				print "Value is not int"
				isint = False
		isint = False
		while isint == False:
			try:
				cuniqcapt = int(raw_input('Current count of unique portals captured: '))
			except ValueError:
				print "Value is not int"
				isint = False
		isint = False
		while isint == False:
			try:
				cdestr = int(raw_input('Current count of destroyed resonators: '))
			except ValueError:
				print "Value is not int"
				isint = False
		isint = False
		while isint == False:
			try:
				cguard = int(raw_input('Current max time portal held in days: '))
			except ValueError:
				print "Value is not int"
				isint = False
