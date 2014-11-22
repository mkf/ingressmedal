# -*- coding: utf-8 -*-
class pastanalyzeoneagent:
	def __init__(self,codename,filepath='defdb.xml',overs=False):
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
	def gainbetweenentries(self,param):
		pastia = self.pastia
		tajmy = self.tajmy
		dictgainpertime = {}
		for i  in tajmy:
			if tajmy.index(i) == 0:
				first = i
			else:
				try:
					dictgainpertime[i] = int(pastia[i][param]) - int(pastia[tajmy[tajmy.index(i)-1]][param])
				except ValueError:
					if pastia[i][param] == 'n':
						pass
					elif pastia[tajmy[tajmy.index(i)-1]][param] == 'n':
						for o in xrange((tajmy.index(i)-1),-1,-1):
							if pastia[tajmy[o]] == 'n':
								pass
							else:
								try:
									dictgainpertime[i] = int(pastia[i][param]) - int(pastia[tajmy[o]][param])
									break
								except ValueError:
									pass
		return {'d': dictgainpertime, 'f': first}

	@staticmethod
	def gainpertime(dgb,first):
		new = {}
		for i in sorted(dgb.keys()):
			if min(sorted(dgb.keys())) == i:
				tajmbetw = int(i) - int(first)
			else:
				tajmbetw = int(i) - int(last)
			last = i
			new[i] = float(float(dgb[i]) / float(tajmbetw))
		return new

	def medalclimbing(self):
		pastia = self.pastia
		from ownlib.clarifydata import clarifydata
		c = clarifydata()
		givba = {}
		for parem in c.thesavelistgrouped['medalthings']:
			givba[parem] = [[],[]]
		for e in sorted(pastia.keys()):
			for s in pastia[e].keys():
				if s in c.thesavelistgrouped['medalthings']:
					try:
						givba[s][1].append(int(pastia[e][s]))
						givba[s][0].append(int(pastia[e]['timed']))
					except:
						pass
		return givba

	@staticmethod
	def propmedalclimbingrelative(wha,color):
		from ownlib.gameinfo import gameinfo
		g = gameinfo()
		new = {}
		for par in wha.keys():
			new[par] = [wha[par][0],[]]
			for i in wha[par][1]:
				if (not((float(float(wha[par][1][wha[par][1].index(i)])/float(g.medaldict[par if par != 'guardnow' else 'guard']['walk'][color]))) > 1)) and (par in new):
					new[par][1].append(float(float(wha[par][1][wha[par][1].index(i)])/float(g.medaldict[par if par != 'guardnow' else 'guard']['walk'][color])))
				else:
					new.pop(par,None)
		return new

	@staticmethod
	def propmedalclimbingabsolute(wha,color):
		from ownlib.gameinfo import gameinfo
		g = gameinfo()
		new = {}
		for par in wha.keys():
			new[par] = [wha[par][0],[]]
			for i in wha[par][1]:
				new[par][1].append(float(float(wha[par][1][wha[par][1].index(i)])/float(g.medaldict[par if par != 'guardnow' else 'guard']['walk'][color])))
		return new

	def givemenewestcurrent(self):
		return self.givemespeccurrent(max(self.givemetimes()))

	def givemetimes(self):
		return self.pastia.keys()

	def givemespeccurrent(self,timed):
		return self.pastia[timed]

	def apclimbing(self):
		pastia = self.pastia
		from gameinfo import gameinfo
		g = gameinfo()
		givba = {}
		givba['ap'] = [[],[]]
		givba['uncomputable']=[[],[]]
		for p in g.outconvtoap:
			givba[p] = [[],[]]
		from singleentry import singleentry
		for e in sorted(pastia.keys()):
			givba['ap'][1].append(int(pastia[e]['ap']))
			givba['ap'][0].append(int(pastia[e]['timed']))
			s = singleentry()
			apcomputable = s.coUNTINGcurapcountable(pastia[e])
			apuncomputable = int(pastia[e]['ap'])-sum(apcomputable.values())
			givba['uncomputable'][1].append(apuncomputable)
			givba['uncomputable'][0].append(int(pastia[e]['timed']))
			for i in apcomputable.keys():
				givba[i][1].append(apcomputable[i])
				givba[i][0].append(int(pastia[e]['timed']))
		return givba

	def apgainavgperdaybetwentrs(self):
		pastia = self.pastia
		from gameinfo import gameinfo
		g = gameinfo()
		givba = {}
		givba['ap'] = [[],[]]
		givba['uncomputable']=[[],[]]
		for p in g.outconvtoap:
			givba[p] = [[],[]]
		from singleentry import singleentry
		for e in sorted(pastia.keys()):
			if sorted(pastia.keys()).index(e)==0:
				pass
			else:
				tb3a = int(e)
				tb3b=int(sorted(pastia.keys())[sorted(pastia.keys()).index(e)-1])
				tb2 = tb3a-tb3b
				tb1 = float(tb2)/3600/24
				timebetween=float(tb1)
				givba['ap'][1].append(float(int(pastia[e]['ap'])-int(pastia[sorted(pastia.keys())[sorted(pastia.keys()).index(e)-1]]['ap']))/timebetween)
				givba['ap'][0].append(int(e))
				s = singleentry()
				apcomputable = s.coUNTINGcurapcountable(pastia[e])
				prevapcomputable = s.coUNTINGcurapcountable(pastia[int(sorted(pastia.keys())[sorted(pastia.keys()).index(e)-1])])
				prevapuncomputable = int(
					int(
						pastia[
							sorted(pastia.keys())[
								sorted(pastia.keys()).index(e)-1
							]
						]['ap']
					)-sum(prevapcomputable.values())
				)
				apuncomputable = int(pastia[e]['ap'])-sum(apcomputable.values())
				givba['uncomputable'][1].append(float(apuncomputable-prevapuncomputable)/timebetween)
				givba['uncomputable'][0].append(int(e))
				for i in apcomputable.keys():
					givba[i][1].append(float(apcomputable[i]-prevapcomputable[i])/timebetween)
					givba[i][0].append(int(e))
		return givba


	def gainpropmedalclimbing(self,wha):
		new = {}
		for par in wha.keys():
			new[par]=[[],[]]
			for indexon in range(0,len(wha[par][0])):
				i = float(wha[par][0][indexon])
				j = float(wha[par][1][indexon])
				if indexon > 0:
					ip = float(wha[par][0][indexon-1])
					jp = float(wha[par][1][indexon-1])
					new[par][0].append(i)
					new[par][1].append((j-jp)/((i-ip)/3600/24))
		return new