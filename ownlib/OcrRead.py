# -*- coding: utf-8 -*-

# TODO: steal some ideas from https://github.com/BlueHerons/StatTracker/blob/master/code/OCR.class.php

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

	@staticmethod
	def prococrad(ocradin):
		# stolen from https://github.com/BlueHerons/StatTracker/blob/master/code/OCR.class.php - Thanks!
		step = 'start'
		elements = []
		import re
		lines = ocradin.split('\n')
		for line in lines:
			if step == 'start':
				oj = re.search(r'^\s*([\d\s\|.egiloqt,]+)\s*AP\s*$',line,re.S|re.I|re.X|re.M)
				if oj is not None:
					step = 'ap'
					elements.append(oj)
			elif step == 'ap' and (re.search(r'^\s*Discovery\s*$',line,re.S|re.I|re.X|re.M) is not None):
				step = 'discovery'
				count = 0
			elif step == 'discovery' and (re.search(r'^\s*Building\s*$',line,re.S|re.I|re.X|re.M) is not None):
				# if only 2 stats, then the agent has (seer == 0)    (0 portals discovered)
				if count == 2:
					temp = elements.pop()
					elements.append('0')
					elements.append(temp)
				step = 'building'
			elif step == 'building' and (re.search(r'^\s*Combat\s*$',line,re.S|re.I|re.X|re.M) is not None): step = 'combat'
			elif step == 'combat' and (re.search(r'^\s*Health\s*$',line,re.S|re.I|re.X|re.M) is not None): step = 'health'
			elif step == 'defense' and (re.search(r'^\s*Missions\s*$',line,re.S|re.I|re.X|re.M) is not None): step = 'missions'
			#elif step == 'discovery':
			#	oj = re.search(r'^\s*([\d\s\|.aegiloqt,]+)\s*(?:XM)?\s*$/sxmi',line,re.S|re.I|re.X|re.M)
			#	if oj is not None:
			#		count+=1
			#		elements.append(oj)
			elif step == 'discovery':
				oj = re.search(r'^\s*([\d\s\|.aegiloqt,]+)\s*(?:XM)?\s*$',line,re.S|re.I|re.X|re.M)
				if oj is not None:
					count+=1
					elements.append(oj)
			elif step == 'building':
				oj = re.search(r'^\s*([\d\s\|.aegiloqt,]+)\s*(?:MUs|XM|km|kln)?\s*$',line,re.S|re.I|re.X|re.M)
				if oj is not None: elements.append(oj)
			elif step == 'combat':
				oj = re.search(r'^\s*([\d\s\|.aegiloqt,]+)\s*$',line,re.S|re.I|re.X|re.M)
				if oj is not None: elements.append(oj)
			elif step == 'health':
				oj = re.search(r'^\s*([\d\s\|.aegiloqt,]+)\s*(?:km|kln)\s*$',line,re.S|re.I|re.X|re.M)
				if oj is not None: elements.append(oj)
			elif step == 'defense':
				oj = re.search(r'^\s*([\d\s\|.aegiloqt,]+)\s*(?:(?:(?:km|kln|MU)-)?(?:days|clays|ilays|cl_ys|__ys|d_ys|_ays|\(l_ys))\s*$',line,re.S|re.I|re.X|re.M)
				if oj is not None: elements.append(oj)
			elif step == 'missions':
				oj = re.search(r'^\s*([\d\s\|.aegiloqt,]+)\s*$',line,re.S|re.I|re.X|re.M)
				if oj is not None: elements.append(oj)
			else:
				oj = re.search(r'^\s*(month|week|now)\s*$',line,re.S|re.I|re.X|re.M)
				if oj is not None: print 'maybe because'; print oj

		elementojn = []
		for i in elements:
			p1 = re.sub('[.]|,|\s/','',i)
			p2 = re.sub('o/i','0',p1)
			p3 = re.sub('\||l|i/i','1',p2)
			p4 = re.sub('q/i','4',p3)
			p5 = re.sub('t/i','7',p4)
			p6 = re.sub('a|e/i','8',p5)
			p7 = re.sub('g/','9',p6)
			pf = p7
			elementojn.append(pf)

		#data = []

		#stats = self.getstats()
		#i = 0

		#for stat in stats: if stat.ocr: data[stat.stat] = elements[i] ; i+=1

		#return data
		return elementojn

	#def