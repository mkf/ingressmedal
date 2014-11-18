# -*- coding: utf-8 -*-
class xmling:
	def __init__(self):
		self.versionhistory = ('0','1.0.1.0')
		self.currentversion = '1.0.1.0'

	def opening(self,filename):
		from xml.etree import ElementTree as ET
		with open(filename,'r') as f:
			tree = ET.parse(f)
		node = tree.find('./base')
		for name, value in node.attrib.items():
			if name == 'versioncreated':
				versionc = value
				if versionc == self.currentversion:
					versioncsame = True
				else:
					versioncsame = False
			elif name == 'versionmodified':
				versionm = value
				if versionm == self.currentversion:
					versionmsame = True
				else:
					versionmsame = False
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
		emptylist = []
		dictback = {'base': base,'modifhist':modifhist,'data': data,'agents': emptylist}
		return dictback

	@staticmethod
	def opendata(base):
		data = base.find('./data')
		agents = []
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



	def appendentry(self,udictofpower,timed,dadict,codename):
		import time
		from xml.etree.ElementTree import SubElement
		dictofpower = udictofpower
		base = dictofpower['base']
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

	@staticmethod
	def saving(base,filename,really=True):
		from xml.etree import ElementTree as ET
		from xml.dom import minidom
		rough_string = ET.tostring(base,'utf-8')
		reparsed = minidom.parseString(rough_string)
		juz = reparsed.toprettyxml(indent="  ")
		if really:
			with open(filename,'w') as f:
				f.write(juz)
		if not really:
			print "We're saving to %s now" % filename
			print ":::::"
			print juz
