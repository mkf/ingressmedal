# -*- coding: utf-8 -*-
from ownlib.gameinfo import gameinfo
from ownlib.xmling import xmling


class Current:
	"""This class applies only to current stats, it doesn't compare anything to the past"""

	def __init__(self, codename, interactiveliness, currorg,zocra,argdod, overs):
		# ------------------------constant definitions----------------
		gameinf = gameinfo()
		self.medaldict = gameinf.medaldict
		self.lvldict = gameinf.lvldict
		self.highestplaceofnoappearance = gameinf.highestplaceofnoappearance
		self.namesforcurapcountable = gameinf.namesforcurapcountable
		# ---------------end of constant definitions-----------------
		from ownlib.interactive import Interactive

		self.overs = overs

		self.current = {}
		self.current.update(zocra)
		for i in currorg.keys():
			if currorg[i] is not None:
				if not currorg[i] == False:
					self.current.update({i: currorg[i]})

		interaktywnosc = Interactive()
		self.interaktywnosc = interaktywnosc
		# noinspection PySimplifyBooleanCheck
		if interactiveliness == False:
			for kluczykoa in interaktywnosc.GivMeCurQSdict().keys():
				try:
					bzdurkaldkfh = str(self.current[kluczykoa])
					if bzdurkaldkfh is None or bzdurkaldkfh == "None":
						print "Interactively is False. There is no %s, exiting." % kluczykoa
						quit()
				except:
					print "Interactively is False. There is no %s, exiting." % kluczykoa
					quit()
			for kluczykoa in interaktywnosc.GivMeCurQUSdict().keys():
				try:
					bzdurkafdhgljsdk = str(self.current[kluczykoa])
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
					bzdurkaldkfh = str(self.current[kluczykoa])
					# print "jesttraj" #debug
					# print bzdurkaldkfh #debug
					# print "----------------" #debug
					if bzdurkaldkfh is None or bzdurkaldkfh == "None" or not (type(int(bzdurkaldkfh)) == int):
						#print type(bzdurkaldkfh)
						kluczykoal.append(str(kluczykoa))
					# print "jestnolnem" #debug
				except:
					kluczykoal.append(str(kluczykoa))
				# print "niema" #debug
			for kluczykoa in interaktywnosc.GivMeCurQUSdict().keys():
				# print kluczykoa #debug
				# Why it doesn't append the kluczykoa at the kluczykoal??
				try:
					bzdurkafdhgljsdk = str(self.current[kluczykoa])
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
		if (range(0, 99999).index(int(ciag)) > 0) or (range(0, 99999).index(int(ciag)) == 0) or isinstance(int(ciag),
																										   int):
			return True
		else:
			return False

	@staticmethod
	def CzyLiczbaZeroDoPiecDziewiatekLUBn(ciag):
		if (range(0, 99999).index(int(ciag)) > 0) or (range(0, 99999).index(int(ciag)) == 0) or (
					str(ciag) == 'n') or isinstance(int(ciag), int):
			return True
		else:
			return False

	@property
	def coUNTINGcurapcountable(self):
		from singleentry import singleentry
		return singleentry().coUNTINGcurapcountable(self.current)

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
		from ownlib.singleentry import singleentry
		return singleentry().minapfromact(name,value,apable)


	@staticmethod
	def calclvlbyap(ap):
		from ownlib.singleentry import singleentry

		return singleentry().calclvlbyap(ap)

	@staticmethod
	def findcurrentmedals(current):
		from ownlib.singleentry import singleentry
		return singleentry().findcurrentmedals(current)


	@staticmethod
	def findcurrentmedalsbycolor(what, cur):
		from ownlib.singleentry import singleentry
		return singleentry().findcurrentmedalsbycolor(what,cur)


	@staticmethod
	def calccountofmedalsonce(what, cur):
		from ownlib.singleentry import singleentry
		return singleentry().calccountofmedalsonce(what,cur)


	@staticmethod
	def calcrealcountofmedalsonce(current, what='current', cur=None):
		from ownlib.singleentry import singleentry
		return singleentry().calcrealcountofmedalsonce(current,what=what,cur=cur)


	@staticmethod
	def calcsomecountofmedalsmulti(once):
		from ownlib.singleentry import singleentry
		return singleentry().calcsomecountofmedalsmulti(once)

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

	@staticmethod
	def calclvlbycol(realcountofmedalsmulti):
		from singleentry import singleentry
		return singleentry().calclvlbycol(realcountofmedalsmulti)

	@staticmethod
	def findaspirujacy(curmedalsbycol, current):
		from singleentry import singleentry
		return singleentry().findaspirujacy(curmedalsbycol,current)

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


	def calcweneedleft(self, lvlbycol):
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

	@staticmethod
	def clarifytowinidleft(weneedleft, lvlbycol):
		winidleft = {}

		for ckolor in weneedleft.keys():
			if type(weneedleft[ckolor]) == int:
				winidleft[ckolor] = (lvlbycol[ckolor], weneedleft[ckolor])
		return winidleft

	def stdouta(self, reallvl, ap, lvlbyap, lvlbymed):
		print " "
		print "Codename: %s      Level: %2d " % (self.codename, reallvl)
		print "AP: %d    lvl_by_AP: %2d " % (ap, lvlbyap)
		if lvlbyap < 16:
			abs = float(float(ap) / float(self.lvldict[lvlbyap + 1]['ap']))
			rel = float(float(ap - self.lvldict[lvlbyap]['ap']) / float(
				self.lvldict[lvlbyap + 1]['ap'] - self.lvldict[lvlbyap]['ap']))
			print "Absolute AP % of the next ({:2}) lvl_by_AP: {:.5%}   Relative AP % of the next ({:2}) lvl_by_AP: {:.5%}".format(
				lvlbyap + 1, abs, lvlbyap + 1, rel)
		print "lvl_by_medals: %2d " % lvlbymed

	@staticmethod
	def stdoutb(lvlbycol):
		for blah in ('silver', 'gold', 'platinum', 'onyx'):
			if not lvlbycol[blah] == 8:
				print "Level for medals' colour %s: %2d" % (blah, lvlbycol[blah])

	def stdoutc(self, lvlbycol, winidleft, realcountofmedalsmulti, aspirmulti, current, curmedals, ):
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
							float(curr * 100) / float(self.medaldict[espir]['walk'][bleh]),
							float(
								float(curr - self.medaldict[espir]['walk'][
									colorpossibilities[colorpossibilities.index(bleh) - 1]]) * 100 / \
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
									float(current[tenover]) * 100 / \
									float(
										self.medaldict[tenover]['walk'][
											colorpossibilities[colorpossibilities.index(curmedals[tenover]) + 1]
										]
									)
								),
								float(
									float(
										current[tenover] - self.medaldict[tenover]['walk'][curmedals[tenover]]) * 100 / \
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
								float(self.medaldict[espir]['walk'][bleh] - curr) * 100 / \
								float(self.medaldict[tenover]['walk'][
									colorpossibilities[colorpossibilities.index(curmedals[tenover]) + 1]
								]),
								float(self.medaldict[espir]['walk'][bleh] - curr) * 100 / \
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
									float(current[tonover]) * 100 / float(self.medaldict[tonover]['walk'][
										colorpossibilities[colorpossibilities.index(curmedals[tonover]) + 1]]),
									float(
										current[tonover] - self.medaldict[tonover]['walk'][curmedals[tonover]]) * 100 / \
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
									float(
										self.medaldict[tenover]['walk'][curmedals[tenover]] - current[tenover]) * 100 / \
									float(
										self.medaldict[tonover]['walk'][
											colorpossibilities[colorpossibilities.index(curmedals[tonover]) + 1]
										]
									),
									float(
										self.medaldict[tenover]['walk'][curmedals[tenover]] - current[
											tenover]) * 100 / float(
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
				# realcountofmedalsmulti[bleh],
				# bleh,
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
		winidleft = self.clarifytowinidleft(weneedleft, lvlbycol)
		self.stdouta(reallvl, ap, lvlbyap, lvlbymed)
		self.stdoutb(lvlbycol)
		self.stdoutc(lvlbycol, winidleft, realcountofmedalsmulti, aspirmulti, current, curmedals)

	# def appendtocsv(self,filename):
	# pass

	def savetoxml(self, filename, timed):
		xmling.justappendentrytoxml(filename, "self.current", timed, self.codename, give=self.current)
