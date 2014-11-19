# -*- coding: utf-8 -*-
from ownlib.clarifydata import clarifydata


class xmling:
	def __init__(self):
		self.versionhistory = ('0','1.0.1.0','1.1','1.2','1.2.1')
		self.currentversion = '1.2.1'
		self.progname = "ingressmedal by ArchieT"

	def opening(self,filename):
		from xml.etree import ElementTree as ET
		with open(filename,'r') as f:
			tree = ET.parse(f)
		#node = tree.find('./base')
		node = tree.getroot()
		for name, value in node.attrib.items():
			if name == 'versioncreated':
				versionc = value
				if versionc == self.currentversion:
					versioncsame = True
				else:
					try:
						self.versionhistory.index(versionc)
					except:
						print "Update your app by cloning https://github.com/ArchieT/ingressmedal.git"
					versioncsame = False
			elif name == 'versionmodified':
				versionm = value
				if versionm == self.currentversion:
					versionmsame = True
				else:
					try:
						self.versionhistory.index(versionm)
					except:
						print "Update your app by cloning https://github.com/ArchieT/ingressmedal.git"
					versionmsame = False
			elif name == 'progname':
				if value != self.progname:
					print "Not our file"
					quit()
		modifhist = node.find('./modifhist')
		return {'base': node,'modifhist':modifhist,'versioncsame': versioncsame,'versionc': versionc,'versionmsame':versionmsame,'versionm':versionm}

	def creating(self):
		import time
		from xml.etree.ElementTree import Element,SubElement
		base = Element('base')
		base.set('versioncreated',str(self.currentversion))
		base.set('versionmodified',str(self.currentversion))
		base.set('timecreated',str(time.time()))
		base.set('timemodified',str(time.time()))
		base.set('progname',self.progname)
		modifhist = SubElement(base,'modifhist')
		mhiste = SubElement(modifhist,'mhiste')
		mhiste.set('versionmodified',str(self.currentversion))
		mhiste.set('timemodified',str(time.time()))
		return {'base': base,'modifhist':modifhist}

	def createdata(self,base):
		import time
		from xml.etree.ElementTree import SubElement
		data = SubElement(base,'data')
		base.set('versionmodified',str(self.currentversion))
		base.set('timemodified',str(time.time()))
		modifhist = base.find('./modifhist')
		mhiste = SubElement(modifhist,'mhiste')
		mhiste.set('versionmodified',str(self.currentversion))
		mhiste.set('timemodified',str(time.time()))
		emptydict = {}
		dictback = {'base': base,'modifhist':modifhist,'data': data,'agents': emptydict}
		return dictback


	def opendata(self,base):
		data = base.find('./data')
		agents = {}
		for agento in data.findall('./agent'):
			codename = agento.attrib.get('codename')
			agents[codename] = agento
		modifhist = base.find('./modifhist')
		return {'base': base,'modifhist':modifhist,'data':data,'agents':agents}

	def createagent(self,udictofpow,codename):
		import time
		from xml.etree.ElementTree import SubElement
		dictofpower = udictofpow
		if codename not in dictofpower['agents']:
			agent = SubElement(dictofpower['data'],'agent')
			agent.set('codename',str(codename))
			dictofpower['agents'][codename] = agent
			dictofpower['base'].set('versionmodified',str(self.currentversion))
			dictofpower['base'].set('timemodified',str(time.time()))
			mhiste = SubElement(dictofpower['modifhist'],'mhiste')
			mhiste.set('versionmodified',str(self.currentversion))
			mhiste.set('timemodified',str(time.time()))
		return dictofpower

	def renameagent(self,udictofpow,before,after):
		import time
		from xml.etree.ElementTree import SubElement
		dictofpower = udictofpow
		if after not in dictofpower['agents']:
			dictofpower['agents'][before].set('codename',after)
			dictofpower['agents'][after] = dictofpower['agents'][before]
			dictofpower['agents'].delete(before)
			dictofpower['base'].set('versionmodified',str(self.currentversion))
			dictofpower['base'].set('timemodified',str(time.time()))
			mhiste = SubElement(dictofpower['modifhist'],'mhiste')
			mhiste.set('versionmodified',str(self.currentversion))
			mhiste.set('timemodified',str(time.time()))
		return dictofpower

	def readingentries(self,dictofpower,codename):
		entryout = {}
		clar = clarifydata()
		for entry in dictofpower['agents'][codename].findall('./entry'):
			entryh = {}
			for par in clar.AskForTheListOfDataToBeSavedFromCurrent:
				entryh[par] = entry.attrib.get(par)
			entryh['timed'] = entry.attrib.get('time')
			entryout[entryh['timed']] = entryh
		return entryout



	def appendentry(self,udictofpower,timed,dadict,codename):
		import time
		from xml.etree.ElementTree import SubElement
		ydictofpower = udictofpower
		base = ydictofpower['base']
		if codename not in ydictofpower['agents']:
			odictofpower = self.createagent(ydictofpower,codename)
			dictofpower = odictofpower
		else: dictofpower = ydictofpower
		agent = dictofpower['agents'][codename]
		e = SubElement(agent,'entry')
		e.set('time',str(timed))
		for s in dadict.keys():
			e.set(str(s),str(dadict[s]))
		base.set('versionmodified',str(self.currentversion))
		base.set('timemodified',str(time.time()))
		modifhist = dictofpower['modifhist']
		mhiste = SubElement(modifhist,'mhiste')
		mhiste.set('versionmodified',str(self.currentversion))
		mhiste.set('timemodified',str(time.time()))
		return dictofpower

	def deleteentry(self,udictofpower,codename):
		pass

	def importfile(self,filename,udictofpower):
		pass

	def saving(self,base,filename,really=True):
		from xml.etree import ElementTree as ET
		from xml.dom import minidom
		rough_string = ET.tostring(base,'utf-8')
		#reparsed = minidom.parseString(rough_string)
		#juz = reparsed.toprettyxml(indent="  ")
		juz = rough_string
		if really:
			with open(filename,'w') as f:
				f.write(juz)
		if not really:
			print "We're saving to %s now" % filename
			print ":::::"
			print juz

	@staticmethod
	def justappendentrytoxml(filepath,giving,timed,codename,give):
		import os
		dadict = {}
		from ownlib.clarifydata import clarifydata
		for i in clarifydata().AskForTheListOfDataToBeSavedFromCurrent:
			dadict[i] = give[i]

		if os.path.isfile(filepath) and os.access(filepath,os.W_OK):
			x = xmling()
			pbd = x.opening(filepath)
			pd = x.opendata(pbd['base'])
			pdic = x.appendentry(pd,timed,dadict,codename)
			x.saving(pdic['base'],filepath)
		elif os.path.isfile(filepath):
			raise IOError
		else:
			x = xmling()
			pbd = x.creating()
			pd = x.createdata(pbd['base'])
			pdic = x.appendentry(pd,timed,dadict,codename)
			x.saving(pdic['base'],filepath)
