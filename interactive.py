class interactive:
	"This is a class of interactively entering your data"
	self.currentquestionsuredict = {
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
	self.currentquestionunsuredict = {
		'photo': "Current count of photos approved to portals (check mail) (number (even if it's 0) or 'n' character if you don't know): ",
		'edit': "Current count of edits approved to portals (check mail) (number (even if it's 0) or 'n' character if you don't know): ",
	}
	currentquestionsuredict = self.currentquestionsuredict
	currentquestionunsuredict = self.currentquestionunsuredict
	def __init__(self):
		ldkfghfdslg = 849
	def gimmecurrentquestionsuredict(self):
		return self.currentquestionsuredict
	def gimmecurrentquestionunsuredict(self):
		return self.currentquestionunsuredict
	def current(self):
		questionsuredict = self.currentquestionsuredict
		questionunsuredict = self.currentquestionunsuredict
		currentdict = {}
		for kluczyk in questionsuredict.keys():
			isint = False
			while isint == False:
				try:
					current[kluczyk] = int(raw_input(questionsuredict[kluczyk]))
					isint = True
				except ValueError:
					print "Value is not int"
					isint = False
		for kluczyk in questionunsuredict.keys():
			isintorn = False
			while isintorn == False:
				phototry = raw_input(questionunsuredict[kluczyk])
				try:
					current[kluczyk] = int(phototry)
					isintorn = True
				except:
					print "Value is not int"
					if phototry == "n":
						current[kluczyk] = 'n'
						print "So you don't know, huh?"
						isintorn = True
					else:
						print "It is neither a number nor 'n', you seriously don't know how to answer such a simple question??"
						isintorn = False
		return currentdict
	def currentwyrywki(self,dawajkeya):
		jestwsure = False
		jestwunsure = False
		for a in self.currentquestionsuredict.keys():
			if a == dawajkeya:
				jestwsure = True
		for a in self.currentquestionunsuredict.keys():
			if a == dawajkeya:
				jestwunsure = True
		if ((jestwsure == True) and (jestwunsure == True)) or ((jestwsure == False) and (jestwunsure == False)):
			print "jestwsure"
			print jestwsure
			print "jestwunsure"
			print jestwunsure
			print " "
			print "Exiting."
			return "Crash"
		elif jestwsure == True:
			isint = False
			while isint == False:
				try:
					zmienna = int(raw_input(self.currentquestionsuredict[dawajkeya]))
					isint = True
				except ValueError:
					print "Value is not int"
					isint = False
		elif jestwunsure == True:
			kluczyk = dawajkeya
			isintorn = False
			while isintorn == False:
				phototry = raw_input(self.currentquestionunsuredict[kluczyk])
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
		return zmienna