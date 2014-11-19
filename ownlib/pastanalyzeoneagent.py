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
		clar = clarifydata().AskForTheListOfDataToBeSavedFromCurrent
		tajmy = sorted(pastia.keys())

	#def