# -*- coding: utf-8 -*-

class Current:
	"""This class applies only to current stats, it doesn't compare anything to the past"""

	def __init__(self, codename, interactiveliness, currorg, argdod, overs):
		#------------------------constant definitions----------------
		from gameinfo import gameinfo
		gameinf = gameinfo()
		self.medaldict = gameinf.medaldict
		self.lvldict = gameinf.lvldict
		self.highestplaceofnoappearance = gameinf.highestplaceofnoappearance
		self.namesforcurapcountable = gameinf.namesforcurapcountable
		#---------------end of constant definitions-----------------
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
		if (range(0, 99999).index(int(ciag)) > 0) or (range(0, 99999).index(int(ciag)) == 0) or isinstance(int(ciag),int):
			return True
		else:
			return False

	@staticmethod
	def CzyLiczbaZeroDoPiecDziewiatekLUBn(ciag):
		if (range(0, 99999).index(int(ciag)) > 0) or (range(0, 99999).index(int(ciag)) == 0) or (str(ciag) == 'n') or isinstance(int(ciag),int):
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


	@staticmethod
	def minapfromact(name, value, apable):
		# value is count of activities to calculate AP
		# name is the identifier of an activity
		# apable is a boolean information whether the activity brings you AP
		if apable:
			# noinspection PyUnreachableCode
			if name == 'seer':
				return value * 1000
			elif name == 'depl':
				# we don't know whether those resonators were deployments or upgrades,
				# so we count'em as AT LEAST upgrades
				return value * 65
			elif name == 'link':
				return value * 313
			elif name == 'field':
				return value * (1250 + 313)
			elif name == 'rech':
				# for each 1000XM recharged you've gained AT LEAST 10AP
				return (value / 1000) * 10
			elif name == 'capt':
				return value * 625
			elif name == 'uniqcapt':
				return value * 625
			elif name == 'destr':
				return value * 75
			else:
				raise ValueError
				return 0
		else:
			return 0


	def calclvlbyap(self, ap):  # |
		for lvltry in range(1, 17):  # |
			if ap >= self.lvldict[lvltry]['ap']:  # |
				lvlbyap = lvltry  # |
		return lvlbyap  # |

	def findcurrentmedals(self, current):
		curmedals = {}
		for medaltry in self.medaldict.keys():
			curmedals[medaltry] = 'nothing'
			for colortry in self.medaldict[medaltry]['walk'].keys():
				if current[medaltry] >= self.medaldict[medaltry]['walk'][colortry]:
					if curmedals[medaltry] == 'nothing':
						curmedals[medaltry] = colortry
					elif (
						self.medaldict[medaltry]['walk'][curmedals[medaltry]] < \
							self.medaldict[medaltry]['walk'][colortry]
					):
						curmedals[medaltry] = colortry
		return curmedals


	def findcurrentmedalsbycolor(self, what, cur):
		curmedalsbycol = {}
		if what == 'current':
			curmedals = self.findcurrentmedals(cur)
		elif what == 'curmedals':
			curmedals = cur
		else:
			raise ValueError
		colorpossibilities = ('bronze', 'silver', 'gold', 'platinum', 'onyx')
		curmedalsbycol['nothing'] = []
		for trycolor in colorpossibilities:
			curmedalsbycol[trycolor] = []
		for trymedal in curmedals.keys():
			curmedalsbycol[curmedals[trymedal]].append(trymedal)
		return curmedalsbycol


	def calccountofmedalsonce(self, what, cur):
		if what == 'current':
			curmedalsbycol = self.findcurrentmedalsbycolor(what, cur)
		elif what == 'curmedals':
			curmedalsbycol = self.findcurrentmedalsbycolor(what, cur)
		elif what == 'curmedalsbycol':
			curmedalsbycol = cur
		else:
			raise ValueError
		colorpossibilities = ('bronze', 'silver', 'gold', 'platinum', 'onyx')
		countofmedalsonce = {}
		for colorpossibility in colorpossibilities:
			countofmedalsonce[colorpossibility] = 0
		for countmedaltry in curmedalsbycol.keys():
			for _ in curmedalsbycol[countmedaltry]:
				countofmedalsonce[countmedaltry] += 1
		return countofmedalsonce


	def calcrealcountofmedalsonce(self, current, what='current', cur=None):
		if what == 'current':
			countofmedalsonce = self.calccountofmedalsonce(what, current)
		elif what == 'curmedals':
			countofmedalsonce = self.calccountofmedalsonce(what, cur)
		elif what == 'curmedalsbycol':
			countofmedalsonce = self.calccountofmedalsonce(what, cur)
		elif what == 'countofmedalsonce':
			countofmedalsonce = cur
		else:
			raise ValueError
		colorpossibilities = ('bronze', 'silver', 'gold', 'platinum', 'onyx')
		realcountofmedalsonce = {}
		for anothercolorpossibility in colorpossibilities:
			if current[anothercolorpossibility] == 'n':
				realcountofmedalsonce[anothercolorpossibility] = countofmedalsonce[anothercolorpossibility]
			elif type(int(current[anothercolorpossibility])) == int:
				realcountofmedalsonce[anothercolorpossibility] = current[anothercolorpossibility]
		return realcountofmedalsonce


	@staticmethod
	def calcsomecountofmedalsmulti(once):
		multi = {
			'bronze': once['bronze'] + once['silver'] + once['gold'] + once['platinum'] + once['onyx'],
			'silver': once['silver'] + once['gold'] + once['platinum'] + once['onyx'],
			'gold': once['gold'] + once['platinum'] + once['onyx'],
			'platinum': once['platinum'] + once['onyx'],
			'onyx': once['onyx']
		}
		return multi

	@staticmethod
	def diffrealvscalculatedmedals(real, calc):
		colorpossibilities = ('bronze', 'silver', 'gold', 'platinum', 'onyx')
		diff = {}
		for color in colorpossibilities:
			diff[color] = real[color] - calc[color]
		return diff

	def generatethereqmedintoselflvldictbtwlvlbymedfir(self, realcountofmedalsmulti):
		colorpossibilities = ('bronze', 'silver', 'gold', 'platinum', 'onyx')
		lvlbymedfir = 8
		for lvlmedtry in range(9, 17):
			medlvltrytab = []
			for possicolor in colorpossibilities:
				try:
					if int(self.lvldict[lvlmedtry][possicolor]) > 0:
						medlvltrytab.append({possicolor: int(self.lvldict[lvlmedtry][possicolor])})
				except KeyError:
					pass
			# self.lvldict[lvlmedtry]['reqmed'] = tuple(medlvltrytab)
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
		return lvlbymedfir

	@staticmethod
	def calcreallvl(bap, bmed):
		for t in range(1, 17):
			if (bap >= t) and (bmed >= t):
				real = t
		return real

	def calclvlbycol(self, realcountofmedalsmulti):
		lvlbycol = {}
		for trykiolor in ('silver', 'gold', 'platinum', 'onyx'):
			lvlbycol[trykiolor] = self.highestplaceofnoappearance[trykiolor]
		for trycollvl in range(9, 17):
			reqmed = self.lvldict[trycollvl]['reqmed']
			for tryreqmed in reqmed.keys():
				if lvlbycol[tryreqmed] < trycollvl:
					if reqmed[tryreqmed] <= realcountofmedalsmulti[tryreqmed]:
						lvlbycol[tryreqmed] = trycollvl
					# print "Poniewaz %d <= %d" % (reqmed[tryreqmed], realcountofmedalsmulti[tryreqmed]) #debug
					# print "Przyszlo %2d do %s" % (trycollvl, tryreqmed) #debug
		return lvlbycol

	def findaspirujacy(self, curmedalsbycol, current):
		aspirujacy = {}
		testulist = []
		colorpossibilitiesnothing = ('nothing', 'bronze', 'silver', 'gold', 'platinum', 'onyx')
		colorpossibilities = ('bronze', 'silver', 'gold', 'platinum', 'onyx')

		for kolor in colorpossibilities:
			if not kolor == 'onyx':
				aspirujacy[kolor] = []

		for kolor in colorpossibilitiesnothing:
			if kolor == 'onyx':
				pass
			else:
				ckolorkis = {1: 'bronze', 2: 'silver', 3: 'gold', 4: 'platinum', 5: 'onyx'}
				ackolorkis = {'nothing': 0, 'bronze': 1, 'silver': 2, 'gold': 3, 'platinum': 4, 'onyx': 5}
				#colowr = colorpossibilities[colorpossibilitiesnothing.index(kolor)]
				colowr = str(ckolorkis[int(ackolorkis[str(kolor)])+1])
				aspirujacy[colowr] = []
				if len(curmedalsbycol[colowr]) > 0:
					for wklej in curmedalsbycol[kolor]:
						aspirujacy[colowr].append(wklej)
						newcolowr = colowr
						newkolor = kolor
						#print "current[wklej]: %s" % current[wklej]
						#print "self.medaldict[wklej]['walk'][newcolowr]: %s" % self.medaldict[wklej]['walk'][newcolowr]
						#print "self.medaldict[wklej]['walk'][newkolor]: %s" % self.medaldict[wklej]['walk'][newkolor]
						#if (
						#	(int(self.medaldict[wklej]['walk'][newkolor])) < (int(current[wklej])) < (int(self.medaldict[wklej]['walk'][newcolowr]))
						#):
						#	aspirujacy[colowr].append(wklej)
						#elif ((int(self.medaldict[wklej]['walk'][newcolowr])) == (int(current[wklej]))):
						#	aspirujacy[colowr].append(wklej)
						#while True:
						#	if (
						#		(int(self.medaldict[wklej]['walk'][newcolowr]) - int(current[wklej]) < 0) or \
						#			(int(current[wklej]) - int(self.medaldict[wklej]['walk'][newkolor]) < 0) or \
						#				(current[wklej] == self.medaldict[wklej]['walk'][newcolowr]) or \
						#					(current[wklej] > self.medaldict[wklej]['walk'][newcolowr]) or \
						#						(current[wklej] < self.medaldict[wklej]['walk'][newkolor])
						#		):
						#		while (
						#			(int(self.medaldict[wklej]['walk'][newcolowr]) - int(current[wklej]) < 0) or \
						#				(int(current[wklej]) - int(self.medaldict[wklej]['walk'][newkolor]) < 0) or \
						#					(current[wklej] == self.medaldict[wklej]['walk'][newcolowr]) or \
						#						(current[wklej] > self.medaldict[wklej]['walk'][newcolowr]) or \
						#							(current[wklej] < self.medaldict[wklej]['walk'][newkolor])
						#		):
						#			if (
						#			(int(self.medaldict[wklej]['walk'][newcolowr] - current[wklej] < 0)) or \
						#				(current[wklej] == self.medaldict[wklej]['walk'][newcolowr]) or \
						#					(current[wklej] > self.medaldict[wklej]['walk'][newcolowr])
						#			):
						#				newkolor = colorpossibilitiesnothing[colorpossibilities.index(newcolowr)]
						#				newcolowr = colorpossibilities[colorpossibilitiesnothing.index(newkolor)]
						#				print "a1 %s %s" % (newkolor, newcolowr)  # debug
						#			elif (
						#			(int(current[wklej]) - int(self.medaldict[wklej]['walk'][newkolor] < 0)) or \
						#				(current[wklej] < self.medaldict[wklej]['walk'][newkolor])
						#			):
						#				newcolowr = colorpossibilities[colorpossibilitiesnothing.index(newkolor)]
						#				newkolor = colorpossibilitiesnothing[colorpossibilities.index(newcolowr)]
						#				print "a2 %s %s" % (newkolor, newcolowr)  # debug
						#			else:
						#				print "Co jest?"
						#		if (
						#			(int(self.medaldict[wklej]['walk'][newcolowr]) - int(current[wklej]) < 0) or \
						#				(int(current[wklej]) - int(self.medaldict[wklej]['walk'][newkolor]) < 0) or \
						#					(current[wklej] == self.medaldict[wklej]['walk'][newcolowr]) or \
						#						(current[wklej] > self.medaldict[wklej]['walk'][newcolowr]) or \
						#							(current[wklej] < self.medaldict[wklej]['walk'][newkolor])
						#		):
						#			if (
						#			(int(self.medaldict[wklej]['walk'][newcolowr] - current[wklej] < 0)) or \
						#				(current[wklej] == self.medaldict[wklej]['walk'][newcolowr]) or \
						#					(current[wklej] > self.medaldict[wklej]['walk'][newcolowr])
						#			):
						#				newkolor = colorpossibilitiesnothing[colorpossibilities.index(newcolowr)]
						#				newcolowr = colorpossibilities[colorpossibilitiesnothing.index(newkolor)]
						#				print "a1 %s %s" % (newkolor, newcolowr)  # debug
						#			elif (
						#			(int(current[wklej]) - int(self.medaldict[wklej]['walk'][newkolor] < 0)) or \
						#				(current[wklej] < self.medaldict[wklej]['walk'][newkolor])
						#			):
						#				newcolowr = colorpossibilities[colorpossibilitiesnothing.index(newkolor)]
						#				newkolor = colorpossibilitiesnothing[colorpossibilities.index(newcolowr)]
						#				print "a2 %s %s" % (newkolor, newcolowr)  # debug
						#			else:
						#				print "Co jest?"
						#	else:
						#		testu = str(colorpossibilities[colorpossibilities.index(str(newcolowr))+1])
						#		testulist.append(testu)
						#		if not (testu == 'onyx'):
						#		#if True:
						#			aspirujacy[testu].append(wklej)
						#			print "QQQQQQQQQQQQ %s : %s %s a testu to %s" % (wklej,newkolor,newcolowr,testu)
						#		break
		return aspirujacy

	@staticmethod
	def findaspirmulti(aspirujacy):
		aspirmulti = {'bronze': [], 'silver': [], 'gold': [], 'platinum': [], 'onyx': []}
		aspirmulti['bronze'].append(aspirujacy['bronze'])
		aspirmulti['silver'].append(aspirujacy['bronze'])
		aspirmulti['gold'].append(aspirujacy['bronze'])
		aspirmulti['platinum'].append(aspirujacy['bronze'])
		aspirmulti['onyx'].append(aspirujacy['bronze'])
		aspirmulti['silver'].append(aspirujacy['silver'])
		aspirmulti['gold'].append(aspirujacy['silver'])
		aspirmulti['platinum'].append(aspirujacy['silver'])
		aspirmulti['onyx'].append(aspirujacy['silver'])
		aspirmulti['gold'].append(aspirujacy['gold'])
		aspirmulti['platinum'].append(aspirujacy['gold'])
		aspirmulti['onyx'].append(aspirujacy['gold'])
		aspirmulti['platinum'].append(aspirujacy['platinum'])
		aspirmulti['onyx'].append(aspirujacy['platinum'])
		aspirmulti['onyx'].append(aspirujacy['onyx'])
		return aspirmulti


	def calcweneedleft(self,lvlbycol):
		weneedleft = {}
		for ckolor in lvlbycol.keys():
			if not (lvlbycol[ckolor] == 16):
				try:
					weneedleft[ckolor] = int(self.lvldict[lvlbycol[ckolor]][ckolor])
				except:
					weneedleft[ckolor] = False
			else:
				weneedleft[ckolor] = False
		return weneedleft

	def clarifytowinidleft(selfself,weneedleft,lvlbycol):
		winidleft = {}

		for ckolor in weneedleft.keys():
			if type(weneedleft[ckolor]) == int:
				winidleft[ckolor] = (lvlbycol[ckolor], weneedleft[ckolor])
		return winidleft

	def stdouta(self,reallvl,ap,lvlbyap,lvlbymed):
		print " "
		print "Codename: %s      Level: %2d " % (self.codename, reallvl)
		print "AP: %d    lvl_by_AP: %2d " % (ap, lvlbyap)
		if lvlbyap < 16:
			abs = float(float(ap)/float(self.lvldict[lvlbyap+1]['ap']))
			rel = float(float(ap-self.lvldict[lvlbyap]['ap'])/float(self.lvldict[lvlbyap+1]['ap']-self.lvldict[lvlbyap]['ap']))
			print "Absolute AP % of the next ({:2}) lvl_by_AP: {:.5%}   Relative AP % of the next ({:2}) lvl_by_AP: {:.5%}".format(lvlbyap+1,abs,lvlbyap+1,rel)
		print "lvl_by_medals: %2d " % lvlbymed

	def stdoutb(self,lvlbycol):
		for blah in ('silver', 'gold', 'platinum', 'onyx'):
			if not lvlbycol[blah] == 8:
				print "Level for medals' colour %s: %2d" % (blah, lvlbycol[blah])

	def stdoutc(self,lvlbycol,winidleft,realcountofmedalsmulti,aspirmulti,current,curmedals,):
		colorpossibilities = ('bronze', 'silver', 'gold', 'platinum', 'onyx')
		for bleh in ('silver', 'gold', 'platinum', 'onyx'):
			if (
								(not lvlbycol[bleh] == 16) and \
									(bleh in winidleft) and \
								(bleh in self.lvldict[lvlbycol[bleh] + 1]) and \
							(self.lvldict[lvlbycol[bleh] + 1][bleh] > realcountofmedalsmulti[bleh])
			):
				print "Next level for the %s colour is %2d" % (bleh, (lvlbycol[bleh] + 1))
				print "You need %1d badges (%1d left), you already have %1d" % (self.lvldict[lvlbycol[bleh] + 1][bleh],
																				self.lvldict[lvlbycol[bleh] + 1][bleh] -
																				realcountofmedalsmulti[bleh],
																				realcountofmedalsmulti[bleh])

				print "Those are the badges which are awaiting promotion to %s:" % bleh
				tabelka = {
					'h': ["Name", "Current", "Left", "Desired lvl", "% Compl. Total", "% Compl. Lvl",
						  "Min AP to compl.", "Description"],
					't': []
				}
				from tabulate import tabulate


				for espirlist in aspirmulti[bleh]:
					for espir in espirlist:
						try:
							if espir == 'guard' and isinstance(int(current['guardnow']), int):
								curr = current['guardnow']
							else:
								curr = current[espir]
						except:
							curr = current[espir]
						if self.medaldict[espir]['over'] and self.overs:
							tabelka['t'].append([
								"__________",
								0,
								0,
								0,
								0,
								0,
								0,
								"_________________"
							])
						tabelka['t'].append([
							str(self.medaldict[espir]['name']),
							curr,
							self.medaldict[espir]['walk'][str(bleh)] - curr,
							self.medaldict[espir]['walk'][bleh],
							float(curr*100) / float(self.medaldict[espir]['walk'][bleh]),
							float(
								float(curr - self.medaldict[espir]['walk'][
									colorpossibilities[colorpossibilities.index(bleh) - 1]])*100 / \
								float(
									self.medaldict[espir]['walk'][bleh] - \
									self.medaldict[espir]['walk'][
										colorpossibilities[colorpossibilities.index(bleh) - 1]]
								)
							),
							self.minapfromact(espir, self.medaldict[espir]['walk'][bleh] - curr,
											  self.medaldict[espir]['apable']),
							self.medaldict[espir]['sdesc']
						])
						if self.medaldict[espir]['over'] and self.overs:
							tenover = self.medaldict[espir]['over']
							tabelka['t'].append([
								str('> ' + str(self.medaldict[tenover]['name'])),
								current[tenover],
								self.medaldict[tenover]['walk'][
									colorpossibilities[colorpossibilities.index(curmedals[tenover]) + 1]
								] - \
								current[tenover],
								self.medaldict[tenover]['walk'][
									colorpossibilities[colorpossibilities.index(curmedals[tenover]) + 1]
								],
								float(
									float(current[tenover])*100 / \
									float(
										self.medaldict[tenover]['walk'][
											colorpossibilities[colorpossibilities.index(curmedals[tenover]) + 1]
										]
									)
								),
								float(
									float(current[tenover] - self.medaldict[tenover]['walk'][curmedals[tenover]])*100 / \
									float(
										self.medaldict[tenover]['walk'][
											colorpossibilities[colorpossibilities.index(curmedals[tenover]) + 1]
										] - self.medaldict[tenover]['walk'][curmedals[tenover]]
									)
								),
								self.minapfromact(tenover, current[tenover], self.medaldict[tenover]['apable']),
								self.medaldict[tenover]['sdesc']
							])
							tabelka['t'].append([
								"> `--> " + curmedals[tenover] + " -> " + colorpossibilities[
									colorpossibilities.index(curmedals[tenover]) + 1],
								0,
								0,
								0,
								float(self.medaldict[espir]['walk'][bleh] - curr)*100 / \
								float(self.medaldict[tenover]['walk'][
									colorpossibilities[colorpossibilities.index(curmedals[tenover]) + 1]
								]),
								float(self.medaldict[espir]['walk'][bleh] - curr)*100 / \
								float(self.medaldict[tenover]['walk'][
								colorpossibilities[colorpossibilities.index(curmedals[tenover]) + 1]
								]),
								self.minapfromact(tenover, self.medaldict[espir]['walk'][bleh] - curr,
												  self.medaldict[tenover]['apable']),
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
									float(current[tonover])*100 / float(self.medaldict[tonover]['walk'][
										colorpossibilities[colorpossibilities.index(curmedals[tonover]) + 1]]),
									float(current[tonover] - self.medaldict[tonover]['walk'][curmedals[tonover]])*100 / \
									float(
										self.medaldict[tonover]['walk'][
											colorpossibilities[colorpossibilities.index(curmedals[tonover]) + 1]
										] - \
										self.medaldict[tonover]['walk'][curmedals[tonover]]
									),
									self.minapfromact(tonover, current[tonover], self.medaldict[tonover]['apable']),
									self.medaldict[tonover]['sdesc']
								])
								tabelka['t'].append([
									">> `--> " + curmedals[tonover] + " -> " + colorpossibilities[
										colorpossibilities.index(curmedals[tonover]) + 1],
									0,
									0,
									0,
									float(self.medaldict[tenover]['walk'][curmedals[tenover]] - current[tenover])*100 / \
									float(
										self.medaldict[tonover]['walk'][
											colorpossibilities[colorpossibilities.index(curmedals[tonover]) + 1]
										]
									),
									float(
										self.medaldict[tenover]['walk'][curmedals[tenover]] - current[tenover])*100 / float(
										self.medaldict[tonover]['walk'][
											colorpossibilities[colorpossibilities.index(curmedals[tonover]) + 1]]),
									self.minapfromact(tenover,
													  self.medaldict[tenover]['walk'][curmedals[tenover]] - current[
														  tenover],
													  self.medaldict[tonover]['apable']),
									"--- By The Way"
								])
							tabelka['t'].append([" ", 0, 0, 0, " ", " ", 0, " "])
				print tabulate(tabelka['t'], headers=tabelka['h'], floatfmt=".5f")
			else:
				# doprintatupel = tuple([
				# 	realcountofmedalsmulti[bleh],
				# 	bleh,
				# 	self.lvldict[lvlbycol[bleh]][bleh],
				# 	lvlbycol[bleh],
				# 	bleh
				# ])
				# print "You have %1d %s badges, you needed %1d for %2d %s lvl, and apparently you don't need'em anymore." % doprintatupel
				pass

	def percentofdest(self):

		current = self.current
		things = self.coUNTINGcurapcountable
		ap = current['ap']
		colorpossibilities = ('bronze', 'silver', 'gold', 'platinum', 'onyx')
		colorpossibilitiesnothing = ('nothing', 'bronze', 'silver', 'gold', 'platinum', 'onyx')
		lvlbyap = self.calclvlbyap(ap)
		curmedals = self.findcurrentmedals(current)
		curmedalsbycol = self.findcurrentmedalsbycolor('curmedals', curmedals)
		countofmedalsonce = self.calccountofmedalsonce('curmedalsbycol', curmedalsbycol)
		realcountofmedalsonce = self.calcrealcountofmedalsonce(current, what='countofmedalsonce', cur=countofmedalsonce)
		countofmedalsmulti = self.calcsomecountofmedalsmulti(countofmedalsonce)
		realcountofmedalsmulti = self.calcsomecountofmedalsmulti(realcountofmedalsonce)
		diffcountofmedalsonce = self.diffrealvscalculatedmedals(realcountofmedalsonce, countofmedalsonce)
		diffcountofmedalsmulti = self.diffrealvscalculatedmedals(realcountofmedalsmulti, countofmedalsmulti)
		lvlbymedfir = self.generatethereqmedintoselflvldictbtwlvlbymedfir(realcountofmedalsmulti)
		reallvl = self.calcreallvl(lvlbyap, lvlbymedfir)
		lvlbycol = self.calclvlbycol(realcountofmedalsmulti)
		lvlbymed = min([lvlbycol[i] for i in ('silver', 'gold', 'platinum', 'onyx')])
		aspirujacy = self.findaspirujacy(curmedalsbycol, current)
		aspirmulti = self.findaspirmulti(aspirujacy)
		weneedleft = self.calcweneedleft(lvlbycol)
		winidleft = self.clarifytowinidleft(weneedleft,lvlbycol)
		self.stdouta(reallvl,ap,lvlbyap,lvlbymed)
		self.stdoutb(lvlbycol)
		self.stdoutc(lvlbycol,winidleft,realcountofmedalsmulti,aspirmulti,current,curmedals)

	#def appendtocsv(self,filename):
	#	pass

	def savetoxml(self,filename,timed,):
		from xmling import xmling
		xmling.justappendentrytoxml(filename,"self.current",timed,codename,give=self.current)
