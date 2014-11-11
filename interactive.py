class Interactive:
	"""This is a class of interactively entering your data"""

	def __init__(self):
		self.currentquestionSdict = {
			'ap': 'Current AP: ',
			'uniqvis': 'Current count of unique portals visited: ',
			'seer': 'Current count of discovered portals: ',
			'hack': 'Current count of hacks: ',
			'depl': 'Current count of deployed resonators: ',
			'link': 'Current count of created links: ',
			'field': 'Current count of created Control Fields: ',
			'rech': 'Current count of recharged XM: ',
			'capt': 'Current count captured portals: ',
			'uniqcapt': 'Current count of unique portals captured: ',
			'destr': 'Current count of destroyed resonators: ',
			'guard': 'Current max time portal held in days: ',
			'destrlink': 'Current count of enemy links destroyed: ',
			'destrfield': 'Current count of enemy Control Fields destroyed: ',
		}
		self.currentquestionUSdict = {
			'photo': "Current count of photos approved to portals (check mail) (number (even if it's 0) or 'n' character if you don't know): ",
			'edit': "Current count of edits approved to portals (check mail) (number (even if it's 0) or 'n' character if you don't know): ",
		}

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
			while isint == False:
				try:
					currentdict[kluczyk] = int(raw_input(questionSdict[kluczyk]))
					isint = True
				except ValueError:
					print "Value is not int"
					isint = False
		for kluczyk in questionUSdict.keys():
			isintorn = False
			while isintorn == False:
				phototry = raw_input(questionUSdict[kluczyk])
				try:
					currentdict[kluczyk] = int(phototry)
					isintorn = True
				except:
					print "Value is not int"
					if phototry == "n":
						currentdict[kluczyk] = 'n'
						print "So you don't know, huh?"
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
		elif jestwS == True:
			isint = False
			while isint == False:
				try:
					zmienna = int(raw_input(self.currentquestionSdict[dawajkeya]))
					isint = True
				except ValueError:
					print "Value is not int"
					isint = False
		elif jestwUS == True:
			kluczyk = dawajkeya
			isintorn = False
			while isintorn == False:
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