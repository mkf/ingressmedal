# -*- coding: utf-8 -*-

class Current:
	"""This class applies only to current stats, it doesn't compare anything to the past"""

	def __init__(self, codename, interactiveliness, currorg, argdod):
		from interactive import Interactive

		self.current = {}
		self.current.update(currorg)

		interaktywnosc = Interactive()
		self.interaktywnosc = interaktywnosc
		if interactiveliness == False:
			for kluczykoa in interaktywnosc.GivMeCurQSdict().keys():
				try:
					bzdurkaldkfh = str(currorg[kluczykoa])
					if bzdurkaldkfh is None or bzdurkaldkfh == "None":
						print "Interactively is False. There is no %s, exiting." % kluczykoa
						quit()
				except:
					print "Interactively is False. There is no %s, exiting." % kluczykoa
					quit()
			for kluczykoa in interaktywnosc.GivMeCurQUSdict().keys():
				try:
					bzdurkafdhgljsdk = str(currorg[kluczykoa])
					if bzdurkafdhgljsdk is None or bzdurkafdhgljsdk == "None":
						print "Interactively is False. There is no %s, exiting." % kluczykoa
						quit()

				except:
					print "Interactively is False. There is no %s, exiting. Next time put in at least an 'n' character." % kluczykoa
					quit()
		elif interactiveliness == True:
			kluczykoal = []
			# print interaktywnosc.GivMeCurQSdict().keys() #debug
			# print interaktywnosc.GivMeCurQUSdict().keys() #debug
			for kluczykoa in interaktywnosc.GivMeCurQSdict().keys():
				# print kluczykoa #debug
				# Why it doesn't append the kluczykoa at the kluczykoal??
				try:
					bzdurkaldkfh = str(currorg[kluczykoa])
					# print "jesttraj" #debug
					# print bzdurkaldkfh #debug
					# print "----------------" #debug
					if bzdurkaldkfh is None or bzdurkaldkfh == "None" or not (type(int(bzdurkaldkfh)) == int):
						print type(bzdurkaldkfh)
						kluczykoal.append(str(kluczykoa))
					# print "jestnolnem" #debug
				except:
					kluczykoal.append(str(kluczykoa))
				# print "niema" #debug
			for kluczykoa in interaktywnosc.GivMeCurQUSdict().keys():
				# print kluczykoa #debug
				# Why it doesn't append the kluczykoa at the kluczykoal??
				try:
					bzdurkafdhgljsdk = str(currorg[kluczykoa])
					# print "jestTrajProba" #debug
					# print bzdurkafdhgljsdk #debug
					# print "--------" #debug
					if bzdurkafdhgljsdk is None or bzdurkafdhgljsdk == "None" or self.CzyLiczbaZeroDoPiecDziewiatekLUBn(
							bzdurkafdhgljsdk) == False:
						kluczykoal.append(str(kluczykoa))
					# print "jestNolnem" #debug
				except:
					kluczykoal.append(str(kluczykoa))
				# print "NiMa" #debug
			# kluczbejs = (interaktywnosc.GivMeCurQSdict().keys() + interaktywnosc.GivMeCurQUSdict().keys()).sort()
			kluczbejs = []
			kluczbejs.extend(interaktywnosc.GivMeCurQSdict().keys())
			kluczbejs.extend(interaktywnosc.GivMeCurQUSdict().keys())
			#print kluczbejs  # debug
			kluczbejs.sort()
			#print kluczbejs  # debug
			kluczykoal.sort()
			# print "kluczbejs" #debug
			# print kluczbejs #debug
			# print "kluczvs" #debug
			# print kluczvs #debug
			# print "kluczykoal" #debug
			#print kluczykoal  # debug
			if kluczbejs == kluczykoal:
				current = interaktywnosc.currentraz()
				self.current.update(current)
			else:
				# if True:
				try:
					current = {}
					for kluczykob in kluczykoal:
						current[kluczykob] = interaktywnosc.currentwyrywki(kluczykob)
					# print current[kluczykob]
					self.current.update(current)
				except:
					pass
		else:
			print "Interactively can't be: "
			try:
				print interactiveliness
			except:
				print "<unreadable>"
			print "   because such value is unsuitable for the situation."
			print "Exiting"
			quit()
		self.codename = codename

	def rjeturncount(self):
		return self.current

	@staticmethod
	def TrueczyFalse(ciag):
		if ((str(ciag == "True")) or (ciag == "y") or (ciag == "yes")) or (
						(ciag == "False") or (ciag == "n") or (ciag == "no")):
			return True
		else:
			return False

	@staticmethod
	def CzyLiczbaZeroDoPiecDziewiatek(ciag):
		if (range(0, 99999).index(int(ciag)) > 0) or (range(0, 99999).index(int(ciag)) == 0):
			return True
		else:
			return False

	@staticmethod
	def CzyLiczbaZeroDoPiecDziewiatekLUBn(ciag):
		if (range(0, 99999).index(int(ciag)) > 0) or (range(0, 99999).index(int(ciag)) == 0) or (str(ciag) == 'n'):
			return True
		else:
			return False

	@property
	def coUNTINGcurapcountable(self):
		current = self.current
		curapcountable = {'seer': int((int(current['seer']) * 1000)),
						  'depllater': int((int((current['depl']) - int(current['capt'])) * 65)),
						  'link': int((int(current['link']) * 313)), 'field': int((int(current['field']) * 1250)),
						  'rechmin': int(((int(current['rech']) / 1000) * 10)),
						  'captres': int((int(current['capt']) * 625)), 'destr': int((int(current['destr']) * 75)),
						  'destrlink': int((int(current['destrlink']) * 187)),
						  'destrfield': int((int(current['destrfield']) * 750))}
		self.namesforcurapcountable = {'seer': "Portals discovered (submitted)",
									   'depllater': "Sure points from deployment of resonators except the capturing one and from upgrading resonators",
									   'link': "Links created", 'field': "Control Fields created",
									   'rechmin': "Minimum AP gained on recharging",
									   'captres': "Capturing portals + first resonator",
									   'destr': "Destroyed resonators", 'destrlink': "Enemy links destroyed",
									   'destrfield': "Enemy Control Fields destroyed",
									   'photo': "Photos added to portals", 'edit': "Edits done to portals' data"}
		if current['photo'] == 'n':
			print "That's your fault you don't know how much AP you've gained on photos."
		else:
			curapcountable['photo'] = (current['photo'] * 500)
		if current['edit'] == 'n':
			print "That's your fault you don't know how much AP you've gained on edits."
		else:
			curapcountable['edit'] = (current['edit'] * 200)
		return curapcountable

	def percent(self):
		import tabulate
		things = self.coUNTINGcurapcountable
		descripts = self.namesforcurapcountable
		percenty = {}
		tabelka = []
		left = self.current['ap']
		for w in sorted(things, key=things.get, reverse=True):
			percenty[w] = str("{:.4%}".format((float(things[w]))/(float(self.current['ap']))))
			left = left - things[w]
			tabelka.append([descripts[w], things[w], percenty[w]])
		tabelka.append(["Uncomputable", left, str("{:.4%}".format((float(left))/(float(self.current['ap']))))])
		print "Total AP: %s" % str(self.current['ap'])
		print tabulate.tabulate(tabelka, headers=["Description", "AP", "Percent of total AP"])
