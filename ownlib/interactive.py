# -*- coding: utf-8 -*-
from ownlib import gameinfo


class Interactive:
	"""This is a class of interactively entering your data"""

	def __init__(self):
		gamei = gameinfo()
		self.currentquestionSdict = gamei.currentquestionSdict
		self.currentquestionUSdict = gamei.currentquestionUSdict

	def GivMeCurQSdict(self):
		return self.currentquestionSdict

	def GivMeCurQUSdict(self):
		return self.currentquestionUSdict

	def currentraz(self):
		questionSdict = self.currentquestionSdict
		questionUSdict = self.currentquestionUSdict
		currentdict = {}
		for kluczyk in questionSdict.keys():
			isint = False
			while not isint:
				try:
					currentdict[kluczyk] = int(raw_input(questionSdict[kluczyk]))
					isint = True
				except ValueError:
					print "Value is not int"
					isint = False
		for kluczyk in questionUSdict.keys():
			isintorn = False
			while not isintorn:
				phototry = raw_input(questionUSdict[kluczyk])
				try:
					currentdict[kluczyk] = int(phototry)
					isintorn = True
				except:
					print "Value is not int"
					if phototry == "n":
						currentdict[kluczyk] = 'n'
						print "You've entered the 'n' letter."
						isintorn = True
					else:
						print "It is neither a number nor 'n', you seriously don't know how to answer such a simple question??"
						isintorn = False
		return currentdict

	def currentwyrywki(self, dawajkeya):
		jestwS = False
		jestwUS = False
		for a in self.currentquestionSdict.keys():
			if a == dawajkeya:
				jestwS = True
		for a in self.currentquestionUSdict.keys():
			if a == dawajkeya:
				jestwUS = True
		if ((jestwS == True) and (jestwUS == True)) or ((jestwS == False) and (jestwUS == False)):
			print "jestwS"
			print jestwS
			print "jestwUS"
			print jestwUS
			print " "
			print "Exiting."
			return "Crash"
		elif jestwS:
			isint = False
			while not isint:
				try:
					zmienna = int(raw_input(self.currentquestionSdict[dawajkeya]))
					isint = True
				except ValueError:
					print "Value is not int"
					isint = False
		elif jestwUS:
			kluczyk = dawajkeya
			isintorn = False
			while not isintorn:
				phototry = raw_input(self.currentquestionUSdict[kluczyk])
				try:
					zmienna = int(phototry)
					isintorn = True
				except:
					print "Value is not int"
					if phototry == "n":
						zmienna = 'n'
						print "So you don't know, huh?"
						isintorn = True
					else:
						print "It is neither a number nor 'n', you seriously don't know how to answer such a simple question??"
						isintorn = False
		print zmienna  # debug
		return zmienna