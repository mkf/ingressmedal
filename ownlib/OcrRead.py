# -*- coding: utf-8 -*-

class OcrRead:
	def __init__(self):
		pass

	@staticmethod
	def ocrad_get(thefile,cache):
		from PIL import Image
		im = Image.open(thefile)
		im.save(cache)
		from os import popen
		#ocradin = system('ocrad -i %s' % cache)
		ocradin = popen('ocrad -i %s' % cache).read()
		#import subprocess
		#proc = subprocess.Popen(["ocrad -i",cache],stdout=subprocess.PIPE,shell=True)
		#(out,err)=proc.communicate()
		#return out
		return ocradin


	def ocradalterproc(self,ocradin):
		elements={}
		import re
		lines = ocradin.split('\n')
		from ocrorigstrs import ocrorigstrs
		o = ocrorigstrs()
		from collections import deque
		so1 = deque(list(o.sortedbyposition))
		while len(so1)>0:
			ej = so1.popleft()
			for line in lines:
				aft = o.origstrsdictaft[ej] if ej in o.origstrsdictaft else r''
				sear = re.search(o.origstrsdictbef[ej]+r'.+'+aft+r'$',line,re.I)
				if sear is not None: elements[ej]=sear.string
		so2 = deque(list(o.sortedbyposition))
		while len(so2)>0:
			ejo = so2.popleft()
			hey = False
			loopinginging=0
			while not hey:
				loopinginging+=1
				if ejo in elements:
					hey = True
				if loopinginging > 100:
					print "My loopinginging is too high thus exiting.",loopinginging
					print a
					quit()
		elementojn = {}
		for eje in elements.keys():
			pbef = re.sub(o.origstrsdictbef[eje],'',elements[eje])
			paft = re.sub(o.origstrsdictaft[eje] if eje in o.origstrsdictaft else r'','',pbef)
			p1 = re.sub('[.]|,|\s/','',paft)
			p2 = re.sub('o','0',p1,re.I)
			p3 = re.sub('\||l|i','1',p2,re.I)
			p4 = re.sub('q','4',p3,re.I)
			p5 = re.sub('t','7',p4,re.I)
			p6 = re.sub('a|e','8',p5,re.I)
			p7 = re.sub('g','9',p6)
			pf = re.sub(r'\D','',p7)
			elementojn[eje] = int(pf)
		return elementojn