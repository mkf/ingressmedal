# -*- coding: utf-8 -*-
class pastanalyzeoneagent:
	def __init__(self,filepath,codename,overs=False):
		from ownlib.gameinfo import gameinfo
		gameinf = gameinfo()
		self.medaldict = gameinf.medaldict
		self.lvldict = gameinf.lvldict
		self.highestplaceofnoappearance = gameinf.highestplaceofnoappearance
		self.namesforcurapcountable = gameinf.namesforcurapcountable
		self.overs = overs
		from xmling import xmling
		x = xmling()
		pbd = x.opening(filepath)
		pd = x.opendata(pbd['base'])
		pastija = x.readingentries(pd,codename)
		pastia = {}
		for keyik in pastija.keys():
			pastia[int(keyik)] = pastija[keyik]
		from clarifydata import clarifydata
		self.clar = clarifydata().AskForTheListOfDataToBeSavedFromCurrent
		tajmy = sorted(pastia.keys())
		self.tajmy = tajmy
		self.pastia = pastia
	def gainpertime(self,param):
		pastia = self.pastia
		tajmy = self.tajmy
		dictgainpertime = {}
		for i  in tajmy:
			if tajmy.index(i) == 0:
				pass
			else:
				try:
					dictgainpertime[i][param] = int(pastia[i][param]) - int(pastia[tajmy[tajmy.index(i)-1]][param])
				except ValueError:
					if pastia[i][param] == 'n':
						pass
					elif pastia[tajmy[tajmy.index(i)-1]][param] == 'n':
						for o in xrange((tajmy.index(i)-1),-1,-1):
							if pastia[tajmy[o]] == 'n':
								pass
							else:
								try:
									dictgainpertime[i][param] = int(pastia[i][param]) - int(pastia[tajmy[o]][param])
									break
								except ValueError:
									pass
		return dictgainpertime