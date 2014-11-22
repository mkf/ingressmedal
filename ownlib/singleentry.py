#  -*- coding: utf-8 -*-

class singleentry:
	def __init__(self):
		pass
	@staticmethod
	def calclvlbyap(ap):
		from ownlib.gameinfo import gameinfo
		for lvltry in range(1, 17):
			if ap >= gameinfo().lvldict[lvltry]['ap']:
				lvlbyap = lvltry
		return lvlbyap

	@staticmethod
	def findcurrentmedals(current):
		curmedals = {}
		from ownlib.gameinfo import gameinfo
		for medaltry in gameinfo().medaldict.keys():
			curmedals[medaltry] = 'nothing'
			for colortry in gameinfo().medaldict[medaltry]['walk'].keys():
				if current[medaltry] >= gameinfo().medaldict[medaltry]['walk'][colortry]:
					if curmedals[medaltry] == 'nothing':
						curmedals[medaltry] = colortry
					elif (
						gameinfo().medaldict[medaltry]['walk'][curmedals[medaltry]] < \
							gameinfo().medaldict[medaltry]['walk'][colortry]
					):
						curmedals[medaltry] = colortry
		return curmedals

	def findcurrentmedalsbycolor(self,what,cur):
		curmedalsbycol = {}
		if what == 'current':
			curmedals = self.findcurrentmedals(cur)
		elif what == 'curmedals':
			curmedals = cur
		elif what == 'curmedalsbycol':
			print "You want what you gave me?"
			raise ValueError
		else:
			raise ValueError
		colorpossibilities = ('bronze', 'silver', 'gold', 'platinum', 'onyx')
		curmedalsbycol['nothing'] = []
		for trycolor in colorpossibilities:
			curmedalsbycol[trycolor] = []
		for trymedal in curmedals.keys():
			curmedalsbycol[curmedals[trymedal]].append(trymedal)
		return curmedalsbycol

	def calccountofmedalsonce(self,what,cur):
		if what == 'current':
			curmedalsbycol = self.findcurrentmedalsbycolor(what, cur)
		elif what == 'curmedals':
			curmedalsbycol = self.findcurrentmedalsbycolor(what, cur)
		elif what == 'curmedalsbycol':
			curmedalsbycol = cur
		else:
			raise ValueError
		colorpossibilities = ('nothing','bronze', 'silver', 'gold', 'platinum', 'onyx')
		countofmedalsonce = {}
		for colorpossibility in colorpossibilities:
			countofmedalsonce[colorpossibility] = 0
		for countmedaltry in curmedalsbycol.keys():
			for _ in curmedalsbycol[countmedaltry]:
				countofmedalsonce[countmedaltry] += 1
		return countofmedalsonce

	@staticmethod
	def minapfromact(name, value, apable):
		# value is count of activities to calculate AP
		# name is the identifier of an activity
		# apable is a boolean information whether the activity brings you AP
		if apable:
			# noinspection PyUnreachableCode,PyUnreachableCode,PyUnreachableCode
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

	def calcrealcountofmedalsonce(self, current, what='current', cur=None):
		if what == 'current':
			countofmedalsonce = self.calccountofmedalsonce(what, current)
		elif what == 'currentbutstr':
			curi = {}
			for i in current.keys():
				if current[i] != 'n':
					curi[i] = int(current[i])
			countofmedalsonce = self.calccountofmedalsonce('current', curi)
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
	def calcreallvl(bap, bmed):
		for t in range(1, 17):
			if (bap >= t) and (bmed >= t):
				real = t
		return real

	@staticmethod
	def calclvlbycol(realcountofmedalsmulti):
		lvlbycol = {}
		from gameinfo import gameinfo
		for trykiolor in ('silver', 'gold', 'platinum', 'onyx'):
			lvlbycol[trykiolor] = gameinfo().highestplaceofnoappearance[trykiolor]
		for trycollvl in range(9, 17):
			reqmed = gameinfo().reqmed(trycollvl)
			for tryreqmed in reqmed.keys():
				if lvlbycol[tryreqmed] < trycollvl:
					if reqmed[tryreqmed] <= realcountofmedalsmulti[tryreqmed]:
						lvlbycol[tryreqmed] = trycollvl
					# print "Poniewaz %d <= %d" % (reqmed[tryreqmed], realcountofmedalsmulti[tryreqmed]) #debug
					# print "Przyszlo %2d do %s" % (trycollvl, tryreqmed) #debug
		return lvlbycol

	@staticmethod
	def calclvlbycol(realcountofmedalsmulti):
		lvlbycol = {}
		from gameinfo import gameinfo
		for trykiolor in ('silver', 'gold', 'platinum', 'onyx'):
			lvlbycol[trykiolor] = gameinfo().highestplaceofnoappearance[trykiolor]
		for trycollvl in range(9, 17):
			reqmed = gameinfo().reqmed(trycollvl)
			for tryreqmed in reqmed.keys():
				if lvlbycol[tryreqmed] < trycollvl:
					if reqmed[tryreqmed] <= realcountofmedalsmulti[tryreqmed]:
						lvlbycol[tryreqmed] = trycollvl
					# print "Poniewaz %d <= %d" % (reqmed[tryreqmed], realcountofmedalsmulti[tryreqmed]) #debug
					# print "Przyszlo %2d do %s" % (trycollvl, tryreqmed) #debug
		return lvlbycol

	@staticmethod
	def findaspirujacy(curmedalsbycol, current):
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
				# colowr = colorpossibilities[colorpossibilitiesnothing.index(kolor)]
				colowr = str(ckolorkis[int(ackolorkis[str(kolor)]) + 1])
				aspirujacy[colowr] = []
				if len(curmedalsbycol[colowr]) > 0:
					for wklej in curmedalsbycol[kolor]:
						aspirujacy[colowr].append(wklej)
						newcolowr = colowr
						newkolor = kolor
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

	@staticmethod
	def calcweneedleft(lvlbycol):
		from gameinfo import gameinfo
		weneedleft = {}
		for ckolor in lvlbycol.keys():
			if not (lvlbycol[ckolor] == 16):
				try:
					weneedleft[ckolor] = int(gameinfo().lvldict[lvlbycol[ckolor]][ckolor])
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

	def coUNTINGcurapcountable(self,current):
		curapcountable = {'seer': int((int(current['seer']) * 1000)),
						  'depllater': int(((int(current['depl']) - int(current['capt'])) * 65)),
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

