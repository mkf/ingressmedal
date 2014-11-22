# -*- coding: utf-8 -*-

class OcrRead:
	def __init__(self):
		pass

	@staticmethod
	def ocrad_get(thefile):
		from PIL import Image
		im = Image.open(thefile)
		import tempfile
		cache = tempfile.NamedTemporaryFile()
		namecache=cache.name
		#print namecache  #debug
		#outpoot = tempfile.TemporaryFile()
		im.save(cache,format='PPM')
		from os import popen
		#ocradin = system('ocrad -i %s' % cache)
		ocradin = popen('ocrad -i %s' % namecache).read()
		#import subprocess
		#outpoot=""
		#proc = subprocess.Popen(["ocrad","-i"],stdout=outpoot,stdin=cache,shell=True)
		#proc.wait()
		#outpoot = ""
		#for linia in proc.stdout:
		#	outpoot+=linia+"\n"
		#print a     # debug
		#return outpoot.read()
		return ocradin


	@staticmethod
	def ocradalterproc(ocradin):
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
					print a   #debug - causes crash and thus I can view the variables in pycharm easily
					quit()
				if ejo == 'seer' and not hey:
					print "Contribute to Ingress and submit at least one portal, please"
					break
				if (ejo == 'destr' or ejo == 'destrlink' or ejo == 'destrfield' or ejo=='neutr') and not hey:
					whatwasdonetothesth = "destroy" if (ejo == 'destr' or ejo=='destrlink' or ejo=='destrfield') else "neutraliz" if ejo=='neutr' else 'something'
					whatshouldbedestroyed = "resonator" if ejo == 'destr' else "enemy link" if ejo == 'destrlink' else "enemy Control Field" if ejo == 'destrfield' else 'portal' if ejo == 'neutr' else "something that was wrong"
					if raw_input("Write 'y' if the player seriously haven't %sed any %s yet, otherwise write 'n': " % (whatwasdonetothesth,whatshouldbedestroyed))=='y':
						print "That's weird, but OK."
						break
		elementojn = {}
		for eje in elements.keys():
			pbef = re.sub(o.origstrsdictbef[eje],'',elements[eje])
			paft = re.sub(o.origstrsdictaft[eje] if eje in o.origstrsdictaft else r'','',pbef)
			p1 = re.sub(r'[.]|,|\s/','',paft)
			p2 = re.sub('o','0',p1,re.I)
			p3 = re.sub(r'\||l|i|I','1',p2,re.I)
			p4 = re.sub('q','4',p3,re.I)
			p5 = re.sub('t','7',p4,re.I)
			p6 = re.sub('a|e','8',p5,re.I)
			p7 = re.sub('g','9',p6)
			p8 = re.sub('O','0',p7)
			pf = re.sub(r'\D','',p8)
			elementojn[eje] = int(pf)
		return elementojn