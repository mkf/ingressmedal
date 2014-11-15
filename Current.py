# -*- coding: utf-8 -*-

class Current:
	"""This class applies only to current stats, it doesn't compare anything to the past"""

	def __init__(self, codename, interactiveliness, currorg, argdod, overs):
		self.medaldict = {
			'uniqvis': {'name': 'Explorer', 'sdesc': 'Uniq visited', 'apable': False,
						'walk': {'bronze': 100, 'silver': 1000, 'gold': 2000, 'platinum': 10000, 'onyx': 30000},
						'over': 'hack', 'sub': False},
			'seer': {'name': 'Seer', 'sdesc': 'Portals discovered', 'apable': True,
					 'walk': {'bronze': 10, 'silver': 20, 'gold': 200, 'platinum': 500, 'onyx': 5000}, 'over': False,
					 'sub': False},
			'hack': {'name': 'Hacker', 'sdesc': 'Hacks', 'apable': False,
					 'walk': {'bronze': 2000, 'silver': 10000, 'gold': 30000, 'platinum': 100000, 'onyx': 200000},
					 'over': False, 'sub': 'uniqvis'},
			'depl': {'name': 'Builder', 'sdesc': 'Resonators deployed', 'apable': True,
					 'walk': {'bronze': 2000, 'silver': 10000, 'gold': 30000, 'platinum': 100000, 'onyx': 200000},
					 'over': False, 'sub': 'capt'},
			'link': {'name': 'Connector', 'sdesc': 'Links created', 'apable': True,
					 'walk': {'bronze': 50, 'silver': 1000, 'gold': 5000, 'platinum': 25000, 'onyx': 100000}, 'over': False,
					 'sub': 'field'},
			'field': {'name': 'Mind Controller', 'sdesc': 'CFields created', 'apable': True,
					  'walk': {'bronze': 100, 'silver': 500, 'gold': 2000, 'platinum': 10000, 'onyx': 40000},
					  'over': 'link', 'sub': False},
			'rech': {'name': 'Recharger', 'sdesc': 'XM Recharged', 'apable': True,
					 'walk': {'bronze': 100000, 'silver': 1000000, 'gold': 3000000, 'platinum': 10000000, 'onyx': 25000000},
					 'over': False, 'sub': False},
			'capt': {'name': 'Liberator', 'sdesc': 'Portals captured', 'apable': True,
					 'walk': {'bronze': 100, 'silver': 1000, 'gold': 5000, 'platinum': 15000, 'onyx': 40000},
					 'over': 'depl', 'sub': 'uniqcapt'},
			'uniqcapt': {'name': 'Pioneer', 'sdesc': 'Uniq captured', 'apable': True,
						 'walk': {'bronze': 20, 'silver': 200, 'gold': 1000, 'platinum': 5000, 'onyx': 20000},
						 'over': 'capt', 'sub': False},
			'destr': {'name': 'Purifier', 'sdesc': 'Resonators destroyed', 'apable': True,
					  'walk': {'bronze': 2000, 'silver': 10000, 'gold': 30000, 'platinum': 100000, 'onyx': 300000},
					  'over': False, 'sub': False},
			'guard': {'name': 'Guardian', 'sdesc': 'Max time portal held', 'apable': False,
					  'walk': {'bronze': 3, 'silver': 10, 'gold': 20, 'platinum': 90, 'onyx': 150}, 'over': False,
					  'sub': False},
		}
		self.lvldict = {
			1: {'ap': 0, 'bene': {'itemy': True, 'xm': 3000, 'rd': 250, 'gamebegun': True}},
			2: {'ap': 2500, 'bene': {'itemy': True, 'xm': 4000, 'rd': 500, 'gamebegun': False}},
			3: {'ap': 20000, 'bene': {'itemy': True, 'xm': 5000, 'rd': 750, 'gamebegun': False}},
			4: {'ap': 70000, 'bene': {'itemy': True, 'xm': 6000, 'rd': 1000, 'gamebegun': False}},
			5: {'ap': 150000, 'bene': {'itemy': True, 'xm': 7000, 'rd': 1250, 'gamebegun': False}},
			6: {'ap': 300000, 'bene': {'itemy': True, 'xm': 8000, 'rd': 1500, 'gamebegun': False}},
			7: {'ap': 600000, 'bene': {'itemy': True, 'xm': 9000, 'rd': 1750, 'gamebegun': False}},
			8: {'ap': 1200000, 'bene': {'itemy': True, 'xm': 10000, 'rd': 2000, 'gamebegun': False}},
			9: {'ap': 2400000, 'silver': 4, 'gold': 1,
				'bene': {'itemy': False, 'xm': 10900, 'rd': 2250, 'gamebegun': False}},
			10: {'ap': 4000000, 'silver': 5, 'gold': 2,
				 'bene': {'itemy': False, 'xm': 11700, 'rd': 2500, 'gamebegun': False}},
			11: {'ap': 6000000, 'silver': 6, 'gold': 5,
				 'bene': {'itemy': False, 'xm': 12400, 'rd': 2750, 'gamebegun': False}},
			12: {'ap': 8400000, 'silver': 7, 'gold': 6,
				 'bene': {'itemy': False, 'xm': 13000, 'rd': 3000, 'gamebegun': False}},
			13: {'ap': 12000000, 'gold': 7, 'platinum': 1,
				 'bene': {'itemy': False, 'xm': 13500, 'rd': 3250, 'gamebegun': False}},
			14: {'ap': 17000000, 'platinum': 2, 'bene': {'itemy': False, 'xm': 13900, 'rd': 3500, 'gamebegun': False}},
			15: {'ap': 24000000, 'platinum': 3, 'bene': {'itemy': False, 'xm': 14200, 'rd': 3750, 'gamebegun': False}},
			16: {'ap': 40000000, 'platinum': 4, 'onyx': 2,
				 'bene': {'itemy': False, 'xm': 14400, 'rd': 4000, 'gamebegun': False}},
		}
		self.namesforcurapcountable = {'seer': "Portals discovered (submitted)",
									   'depllater': "Sure points from deployment of resonators except the capturing one and from upgrading resonators",
									   'link': "Links created", 'field': "Control Fields created",
									   'rechmin': "Minimum AP gained on recharging",
									   'captres': "Capturing portals + first resonator",
									   'destr': "Destroyed resonators", 'destrlink': "Enemy links destroyed",
									   'destrfield': "Enemy Control Fields destroyed",
									   'photo': "Photos added to portals", 'edit': "Edits done to portals' data"}
		from interactive import Interactive

		self.overs = overs

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
			# print kluczbejs  # debug
			kluczbejs.sort()
			# print kluczbejs  # debug
			kluczykoal.sort()
			# print "kluczbejs" #debug
			# print kluczbejs #debug
			# print "kluczvs" #debug
			# print kluczvs #debug
			# print "kluczykoal" #debug
			# print kluczykoal  # debug
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
						  'link': int((int(current['link']) * 313)),
						  'field': int((int(current['field']) * 1250)),
						  'rechmin': int(((int(current['rech']) / 1000) * 10)),
						  'captres': int((int(current['capt']) * 625)),
						  'destr': int((int(current['destr']) * 75)),
						  'destrlink': int((int(current['destrlink']) * 187)),
						  'destrfield': int((int(current['destrfield']) * 750))}
		if current['photo'] == 'n':
			print "That's your fault you don't know how much AP you've gained on photos."
		else:
			curapcountable['photo'] = (current['photo'] * 500)
		if current['edit'] == 'n':
			print "That's your fault you don't know how much AP you've gained on edits."
		else:
			curapcountable['edit'] = (current['edit'] * 200)
		return curapcountable

	def percentofap(self):
		things = self.coUNTINGcurapcountable
		descripts = self.namesforcurapcountable
		percenty = {}
		tabelka = []
		left = self.current['ap']
		for w in sorted(things, key=things.get, reverse=True):
			percenty[w] = str("{:.4%}".format((float(things[w])) / (float(self.current['ap']))))
			left -= things[w]
			tabelka.append([descripts[w], things[w], percenty[w]])
		tabelka.append(["Uncomputable", left, str("{:.4%}".format((float(left)) / (float(self.current['ap']))))])
		print "Total AP: %s" % str(self.current['ap'])
		from tabulate import tabulate

		print tabulate(tabelka, headers=["Description", "AP", "Percent of total AP"])

	def percentofdest(self):
		def minapfromact(name, value, apable):
			if apable:
				if name == 'seer':
					return value * 1000
				elif name == 'depl':
					return value * 65
				elif name == 'link':
					return value * 313
				elif name == 'field':
					return value * 1563
				elif name == 'rech':
					return (value / 1000) * 10
				elif name == 'capt':
					return value * 625
				elif name == 'uniqcapt':
					return value * 625
				elif name == 'destr':
					return value * 75
				else:
					return 0
					raise ValueError
			else:
				return 0

		current = self.current
		things = self.coUNTINGcurapcountable
		ap = current['ap']
		colorpossibilities = ('bronze', 'silver', 'gold', 'platinum', 'onyx')
		colorpossibilitiesnothing = ('nothing', 'bronze', 'silver', 'gold', 'platinum', 'onyx')
		for lvltry in range(1, 17):
			if ap >= self.lvldict[lvltry]['ap']:
				lvlbyap = lvltry
		curmedals = {}
		curmedalsbycol = {}
		for medaltry in self.medaldict.keys():
			curmedals[medaltry] = 'nothing'
			for colortry in self.medaldict[medaltry]['walk'].keys():
				if current[medaltry] >= self.medaldict[medaltry]['walk'][colortry]:
					if curmedals[medaltry] == 'nothing':
						curmedals[medaltry] = colortry
					elif self.medaldict[medaltry]['walk'][curmedals[medaltry]] < self.medaldict[medaltry]['walk'][
						colortry]:
						curmedals[medaltry] = colortry
		curmedalsbycol['nothing'] = []
		for trycolor in colorpossibilities:
			curmedalsbycol[trycolor] = []
		for trymedal in curmedals.keys():
			curmedalsbycol[curmedals[trymedal]].append(trymedal)


		# for trykolor in colorpossibilities:
		# if int(colorpossibilities.index(trykolor)) >= int(colorpossibilities.index(trycolor)):
		# if
		# curmedalsbycol[trycolor].append(trymedal)
		countofmedalsonce = {}
		for colorpossibility in colorpossibilities:
			countofmedalsonce[colorpossibility] = 0
		for countmedaltry in curmedalsbycol.keys():
			for obiekt in curmedalsbycol[countmedaltry]:
				countofmedalsonce[countmedaltry] += 1
		# countofmedalsmulti = {}
		realcountofmedalsonce = {}
		# realcountofmedalsmulti = {}
		for anothercolorpossibility in colorpossibilities:
			if current[anothercolorpossibility] == 'n':
				realcountofmedalsonce[anothercolorpossibility] = countofmedalsonce[anothercolorpossibility]
			elif type(int(current[anothercolorpossibility])) == int:
				realcountofmedalsonce[anothercolorpossibility] = current[anothercolorpossibility]
		# for colorpossibilityonceagain in colorpossibilities:
		# countofmedalsmulti[colorpossibilityonceagain] = 0
		# realcountofmedalsmulti[colorpossibilityonceagain] = 0
		# for positionofcolor in range(0,(colorpossibilities.index(colorpossibilityonceagain)+1)):
		# countofmedalsmulti[colorpossibilityonceagain] += countofmedalsonce[colorpossibilities[positionofcolor]]
		#		realcountofmedalsmulti[colorpossibilityonceagain] += realcountofmedalsonce[colorpossibilities[positionofcolor]]
		como = countofmedalsonce
		romo = realcountofmedalsonce
		countofmedalsmulti = {
			'bronze': como['bronze'] + como['silver'] + como['gold'] + como['platinum'] + como['onyx'],
			'silver': como['silver'] + como['gold'] + como['platinum'] + como['onyx'],
			'gold': como['gold'] + como['platinum'] + como['onyx'],
			'platinum': como['platinum'] + como['onyx'],
			'onyx': como['onyx']
		}
		realcountofmedalsmulti = {
			'bronze': romo['bronze'] + romo['silver'] + romo['gold'] + romo['platinum'] + romo['onyx'],
			'silver': romo['silver'] + romo['gold'] + romo['platinum'] + romo['onyx'],
			'gold': romo['gold'] + romo['platinum'] + romo['onyx'],
			'platinum': romo['platinum'] + romo['onyx'],
			'onyx': romo['onyx']
		}
		diffcountofmedalsonce = {}
		diffcountofmedalsmulti = {}
		for yetanothercolorpossibility in colorpossibilities:
			diffcountofmedalsmulti[yetanothercolorpossibility] = realcountofmedalsmulti[yetanothercolorpossibility] - \
																 countofmedalsmulti[yetanothercolorpossibility]
			diffcountofmedalsonce[yetanothercolorpossibility] = realcountofmedalsonce[yetanothercolorpossibility] - \
																countofmedalsonce[yetanothercolorpossibility]
		lvlbymedfir = 8
		for lvlmedtry in range(9, 17):
			medlvltrytab = []
			for possicolor in colorpossibilities:
				try:
					if int(self.lvldict[lvlmedtry][possicolor]) > 0:
						medlvltrytab.append({possicolor: int(self.lvldict[lvlmedtry][possicolor])})
				except KeyError:
					pass
			#self.lvldict[lvlmedtry]['reqmed'] = tuple(medlvltrytab)
			self.lvldict[lvlmedtry]['reqmed'] = {}
			for a in medlvltrytab:
				self.lvldict[lvlmedtry]['reqmed'].update(a)
			probamedlvltrytabtry = 1
			for medlvltrytabtry in medlvltrytab:
				for keymedlvltrytabtry in medlvltrytabtry.keys():
					if medlvltrytabtry[keymedlvltrytabtry] > realcountofmedalsmulti[keymedlvltrytabtry]:
						probamedlvltrytabtry = 0
			if probamedlvltrytabtry == 1:
				lvlbymedfir = lvlmedtry
		for tryreallvl in range(1, 17):
			if (lvlbyap >= tryreallvl) and (lvlbymedfir >= tryreallvl):
				reallvl = tryreallvl
		lvlbycolfir = {}
		for znowucolorpossible in colorpossibilities:
			lvlbycolfir[znowucolorpossible] = 8
			for trycollvl in range(9, 17):
				if znowucolorpossible == 'brown':
					lvlbycolfir[znowucolorpossible] = trycollvl
					break
				elif znowucolorpossible not in self.lvldict[trycollvl]:
					if lvlbycolfir[znowucolorpossible] == (trycollvl - 1):
						lvlbycolfir[znowucolorpossible] = trycollvl

					#znowuwywu = False
					#zunwowuwuy = colorpossibilities.index(znowucolorpossible)
					#zenwowuwu = zunwowuwuy
					#while ((znowuwywu == False) and (zenwowuwu <= 4)):
					#	if colorpossibilities[zenwowuwu] in self.lvldict[trycollvl]:
					#		uzynwowu = colorpossibilities[zenwowuwu]
					#		if
					#			znowuwywu = True
					#	zenwowuwu += 1
		lvlbycol = {}
		for trykiolor in ('silver', 'gold', 'platinum', 'onyx'):
			lvlbycol[trykiolor] = 8
		for trycollvl in range(9, 17):
			reqmed = self.lvldict[trycollvl]['reqmed']
			for tryreqmed in reqmed.keys():
				if lvlbycol[tryreqmed] < trycollvl:
					if reqmed[tryreqmed] <= realcountofmedalsmulti[tryreqmed]:
						lvlbycol[tryreqmed] = trycollvl
						print "Poniewaz %d <= %d" % (reqmed[tryreqmed], realcountofmedalsmulti[tryreqmed])
						print "Przyszlo %2d do %s" % (trycollvl, tryreqmed)
		lvlbymed = min(lvlbycol.values())


		#elif int(self.lvldict[trycollvl][znowucolorpossible]) <= realcountofmedalsmulti[znowucolorpossible]:
		#	lvlbycol[znowucolorpossible] = trycollvl
		#	print "Poszlo %2d do %s" % (trycollvl,znowucolorpossible)
		#else:
		#	lvlbycol[znowucolorpossible] = 8
		aspirujacy = {}
		#for kolor in colorpossibilities:
		#	aspirujacy[kolor] = []
		#	if kolor == 'bronze':
		#		if len(curmedalsbycol['nothing']) > 0:
		#			for wklej in curmedalsbycol[kolor]:
		#				aspirujacy[kolor].append(wklej)
		#	else:
		#		if len(curmedalsbycol[colorpossibilities[colorpossibilities.index(kolor) - 1]]) > 0:
		#			for wklej in curmedalsbycol[colorpossibilities[colorpossibilities.index(kolor) - 1]]:
		#				aspirujacy[kolor].append(wklej)

		for kolor in colorpossibilitiesnothing:
			if kolor == 'onyx':
				pass
			else:
				colowr = colorpossibilities[colorpossibilitiesnothing.index(kolor)]
				aspirujacy[colowr] = []
				if len(curmedalsbycol[colowr])>0:
					for wklej in curmedalsbycol[kolor]:
						newcolowr = colowr
						newkolor = kolor
						print "current[wklej]: %s" % current[wklej]
						print "self.medaldict[wklej]['walk'][newcolowr]: %s" % self.medaldict[wklej]['walk'][newcolowr]
						print "self.medaldict[wklej]['walk'][newkolor]: %s" % self.medaldict[wklej]['walk'][newkolor]
						while (
							(self.medaldict[wklej]['walk'][newcolowr]-current[wklej]<0) or
							(current[wklej]-self.medaldict[wklej]['walk'][newkolor]<0) or
							(current[wklej]==self.medaldict[wklej]['walk'][newcolowr]) or
							(current[wklej]>self.medaldict[wklej]['walk'][newcolowr]) or
							(current[wklej]<self.medaldict[wklej]['walk'][newkolor])
						):
							if (
								(self.medaldict[wklej]['walk'][newcolowr]-current[wklej]<0) or
								(current[wklej]==self.medaldict[wklej]['walk'][newcolowr]) or
								(current[wklej]>self.medaldict[wklej]['walk'][newcolowr])
							):
								newkolor = colorpossibilitiesnothing[colorpossibilities.index(newcolowr)]
								newcolowr = colorpossibilities[colorpossibilitiesnothing.index(newkolor)]
								print "a1 %s %s" % (newkolor,newcolowr)  #debug
							elif (
								(current[wklej]-self.medaldict[wklej]['walk'][newkolor]<0) or
								(current[wklej]<self.medaldict[wklej]['walk'][newkolor])
							):
								newcolowr = colorpossibilities[colorpossibilitiesnothing.index(newkolor)]
								newkolor = colorpossibilitiesnothing[colorpossibilities.index(newcolowr)]
								print "a2 %s %s" % (newkolor,newcolowr)  #debug
							else:
								print "Co jest?"
						aspirujacy[newcolowr].append(wklej)
				


		aspirmulti = {'bronze': [], 'silver': [], 'gold': [], 'platinum': [], 'onyx': []}
		#for kolorek in colorpossibilities:
		#	aspirmulti[kolorek] = []
		#	subkolorex = []
		#	for subkolorextry in range(0,colorpossibilities.index(kolorek)):
		#		subkolorex.append(colorpossibilities[subkolorextry])
		#	for subkolorek in subkolorex:
		#		aspirmulti[kolorek].extend(aspirujacy[subkolorek])
		#ckolorpo = list(colorpossibilities)
		#possible = True
		#while possible:
		#	try:
		#		cekol = ckolorpo.popleft()
		#		aspirmulti[cekol] = []
		#		aspirmulti[cekol].append(aspirujacy[cekol])
		#		for i in ckolorpo:
		#			aspirmulti[cekol].append(aspirujacy[i])
		#		possible = True
		#	except:
		#		possible = False
		aspirmulti['bronze'].append(aspirujacy['bronze'])
		aspirmulti['bronze'].append(aspirujacy['silver'])
		aspirmulti['bronze'].append(aspirujacy['gold'])
		aspirmulti['bronze'].append(aspirujacy['platinum'])
		aspirmulti['bronze'].append(aspirujacy['onyx'])
		aspirmulti['silver'].append(aspirujacy['silver'])
		aspirmulti['silver'].append(aspirujacy['gold'])
		aspirmulti['silver'].append(aspirujacy['platinum'])
		aspirmulti['silver'].append(aspirujacy['onyx'])
		aspirmulti['gold'].append(aspirujacy['gold'])
		aspirmulti['gold'].append(aspirujacy['platinum'])
		aspirmulti['gold'].append(aspirujacy['onyx'])
		aspirmulti['platinum'].append(aspirujacy['platinum'])
		aspirmulti['platinum'].append(aspirujacy['onyx'])
		aspirmulti['onyx'].append(aspirujacy['onyx'])

		#for ckolor in colorpossibilities:
		#	for lewel in lvlbycol.keys():
		#		if lvlbycol[lewel] < 16:
		#			for colorofcon in self.lvldict[lvlbycol[lewel]][lewel]
		weneed = {}
		for ckolor in lvlbycol.keys():
			if not (lvlbycol[ckolor] == 16):
				try:
					weneed[ckolor] = int(self.lvldict[lvlbycol[ckolor]][ckolor])
				except:
					weneed[ckolor] = False
			else:
				weneed[ckolor] = False
		winid = {}

		for ckolor in weneed.keys():
			if type(weneed[ckolor]) == int:
				winid[ckolor] = (lvlbycol[ckolor], weneed[ckolor])

		print "Codename: %s      Level: %2d " % (self.codename, reallvl)
		print "AP: %d    lvl_by_AP: %2d " % (ap, lvlbyap)
		print "lvl_by_medals: %2d " % lvlbymed
		for blah in ('silver', 'gold', 'platinum', 'onyx'):
			if not lvlbycol[blah] == 8:
				print "Level for medals' colour %s: %2d" % (blah, lvlbycol[blah])

		tabela = []

		for bleh in ('silver', 'gold', 'platinum', 'onyx'):
			if not lvlbycol[bleh] == 16 and (bleh in winid) and (bleh in self.lvldict[lvlbycol[bleh] + 1]) and (
				self.lvldict[lvlbycol[bleh] + 1][bleh] > realcountofmedalsmulti[bleh]):
				print "Next level for the %s colour is %2d" % (bleh, (lvlbycol[bleh] + 1))
				print "You need %1d badges (%1d left), you already have %1d" % (self.lvldict[lvlbycol[bleh] + 1][bleh],
																				self.lvldict[lvlbycol[bleh] + 1][bleh] -
																				realcountofmedalsmulti[bleh],
																				realcountofmedalsmulti[bleh])

				print "Those are the badges which are awaiting promotion:"
				tabelka = {
					'h': ["Name", "Current", "Left", "Next lvl", "% Completed Total", "% Completed Lvl",
						  "Min AP to complete", "Description"],
					't': []
				}
				from tabulate import tabulate


				for espirlist in aspirmulti[bleh]:
					for espir in espirlist:
						try:
							if espir == 'guard' and isinstance(int(current['guardnow']),int):
								curr = current['guardnow']
							else:
								curr = current[espir]
						except:
							curr = current[espir]
						tabelka['t'].append([
   							str(self.medaldict[espir]['name']),
							curr,
							self.medaldict[espir]['walk'][str(bleh)] - curr,
							self.medaldict[espir]['walk'][bleh],
							float(curr) / float(self.medaldict[espir]['walk'][bleh]),
							float(curr - self.medaldict[espir]['walk'][colorpossibilities[colorpossibilities.index(bleh) - 1]]) / float(self.medaldict[espir]['walk'][bleh] - self.medaldict[espir]['walk'][colorpossibilities[colorpossibilities.index(bleh) - 1]]),
							minapfromact(espir, self.medaldict[espir]['walk'][bleh] - curr,self.medaldict[espir]['apable']),
							self.medaldict[espir]['sdesc']
						])
						if self.medaldict[espir]['over'] and self.overs:
							tenover = self.medaldict[espir]['over']
							tabelka['t'].append([
								str('> ' + str(self.medaldict[tenover]['name'])),
								current[tenover],
								self.medaldict[tenover]['walk'][colorpossibilities[colorpossibilities.index(curmedals[tenover]) + 1]] - current[tenover],
								self.medaldict[tenover]['walk'][colorpossibilities[colorpossibilities.index(curmedals[tenover]) + 1]],
								float(current[tenover]) / float(self.medaldict[tenover]['walk'][colorpossibilities[colorpossibilities.index(curmedals[tenover]) + 1]]),
								float(current[tenover] - self.medaldict[tenover]['walk'][curmedals[tenover]]) / float(self.medaldict[tenover]['walk'][colorpossibilities[colorpossibilities.index(curmedals[tenover]) + 1]] -self.medaldict[tenover]['walk'][curmedals[tenover]]),
								minapfromact(tenover, current[tenover], self.medaldict[tenover]['apable']),
								self.medaldict[tenover]['sdesc']
							])
							tabelka['t'].append([
								"> `--> " + curmedals[tenover] + " -> " + colorpossibilities[colorpossibilities.index(curmedals[tenover]) + 1],
								0,
								0,
								0,
								float(self.medaldict[espir]['walk'][bleh] - curr) / float(self.medaldict[tenover]['walk'][colorpossibilities[colorpossibilities.index(curmedals[tenover]) + 1]]),
								float(self.medaldict[espir]['walk'][bleh] - curr) / float(self.medaldict[tenover]['walk'][colorpossibilities[colorpossibilities.index(curmedals[tenover]) + 1]]),
								minapfromact(tenover, self.medaldict[espir]['walk'][bleh] - curr,self.medaldict[tenover]['apable']),
								"  --- By The Way"
							])
							if self.medaldict[tenover]['over']:
								tonover = self.medaldict[tenover]['over']
								tabelka['t'].append([
									'>> ' + str(self.medaldict[tonover]['name']),
									current[tonover],
									self.medaldict[tonover]['walk'][
										colorpossibilities[colorpossibilities.index(curmedals[tonover]) + 1]] - current[
										tonover],
									self.medaldict[tonover]['walk'][
										colorpossibilities[colorpossibilities.index(curmedals[tonover]) + 1]],
									float(current[tonover]) / float(self.medaldict[tonover]['walk'][
										colorpossibilities[colorpossibilities.index(curmedals[tonover]) + 1]]),
									float(current[tonover] - self.medaldict[tonover]['walk'][curmedals[tonover]]) / float(
										self.medaldict[tonover]['walk'][
											colorpossibilities[colorpossibilities.index(curmedals[tonover]) + 1]] -
										self.medaldict[tonover]['walk'][curmedals[tonover]]),
									minapfromact(tonover, current[tonover], self.medaldict[tonover]['apable']),
									self.medaldict[tonover]['sdesc']
								])
								tabelka['t'].append([
									">> `--> " + curmedals[tonover] + " -> " + colorpossibilities[
										colorpossibilities.index(curmedals[tonover]) + 1],
									0,
									0,
									0,
									float(self.medaldict[tenover]['walk'][curmedals[tenover]] - current[tenover]) / float(
										self.medaldict[tonover]['walk'][
											colorpossibilities[colorpossibilities.index(curmedals[tonover]) + 1]]),
									float(self.medaldict[tenover]['walk'][curmedals[tenover]] - current[tenover]) / float(
										self.medaldict[tonover]['walk'][
											colorpossibilities[colorpossibilities.index(curmedals[tonover]) + 1]]),
									minapfromact(tenover,
												 self.medaldict[tenover]['walk'][curmedals[tenover]] - current[tenover],
												 self.medaldict[tonover]['apable']),
									"--- By The Way"
								])
							tabelka['t'].append([" ", 0, 0, 0, " ", " ", 0, " "])
				print tabulate(tabelka['t'], headers=tabelka['h'], floatfmt=".5f")
			else:
				#print "You have %1d %s badges, you needed %1d for %2d %s lvl, and apparently you don't need'em anymore." % (realcountofmedalsmulti[bleh],bleh,self.lvldict[lvlbycol[bleh]][bleh],lvlbycol[bleh],bleh)
				pass