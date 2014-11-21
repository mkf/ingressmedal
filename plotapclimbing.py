#!/usr/bin/python2.7
#  -*- coding: utf-8 -*-
import argparse
from ownlib.pastanalyzeoneagent import pastanalyzeoneagent
def TrueOrFalse(ciag):
	if (ciag == "True") or (ciag == "y") or (ciag == "yes"):
		return True
	elif (ciag == "False") or (ciag == "n") or (ciag == "no"):
		return False
	else:
		raise argparse.ArgumentTypeError('It is not True nor False, y nor n, yes nor no. Although it had to.')

argh = argparse.ArgumentParser()
argh.add_argument('-f','--dbfilepath',type=str,help="Specify dabatase file",default='defdb.xml')
#argh.add_argument('-w','--writeimg',action='store_true',help="Write chart to image file specified in '-i'")
#argh.add_argument('-i','--imgfile',type=argparse.FileType(mode='w'),help="Specify png file to save the chart to")
#argh.add_argument('-j','--nogui',action='store_true',help='Run without pyplot GUI')
argh.add_argument('-y','--dbtype',type=str,help="Specify database type",default='xml',choices=('xml','csv'))
argh.add_argument('-n','--codename',type=str,help="Enter codename (soon you will be able to use it multiple times",required=True)
argh.add_argument('-l','--goallvl',type=int,help="What level are you climbing to?",choices=range(2,17))
parmetry = vars(argh.parse_args())

codename = parmetry['codename']

if parmetry['dbfilepath']:
	pa = pastanalyzeoneagent(codename,filepath=str(parmetry['dbfilepath']))
else:
	pa = pastanalyzeoneagent(codename)

from ownlib.clarifydata import clarifydata
clar = clarifydata()
from ownlib.gameinfo import gameinfo
ginf = gameinfo()
clrs = clar.colorsqua

barck = pa.apclimbing()
back = {}
for i in barck.keys():
	if not(len(barck[i][1]) == 0):
		back[i] = barck[i]
dictclrs = {}
for i in range(0,len(back.keys())):
	dictclrs[sorted(back.keys())[i]] = clrs[i]

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
#for i in back.keys():
#	for o in range(0,len(pa.givemetimes())):
#		plt.plot(back[i][0][o],back[i][1][o],color=dictclrs[i])
plotting = {}
fig, ax = plt.subplots()
for i in back.keys():
	plotting[i] = plt.plot(back[i][0],back[i][1],color=dictclrs[i],linewidth=2.0,label=ginf.medaldict[i if i != 'guardnow' else 'guard']['name'])
from matplotlib.font_manager import FontProperties
fontP = FontProperties()
fontP.set_size('small')
ax.legend(bbox_to_anchor=(1, 0.5), fancybox=True, shadow=True, loc='center left', ncol=1, prop=fontP)
plt.axis([min(pa.givemetimes()),max(pa.givemetimes()),0,max(back['ap'][1])])
plt.title('AP')
plt.ylabel('Percent of %s medal' % coler)
def dtformater(x,pos): from datetime import datetime; return datetime.utcfromtimestamp(int(x)).isoformat(sep='\n')
def kiloformater(x,pos): return '%2.fk' % (x/1000)
ax.yaxis.set_major_formatter(FuncFormatter(kiloformater))
ax.xaxis.set_major_formatter(FuncFormatter(dtformater))
#if not parmetry['nogui']:
plt.show()
#if parmetry['writeimg']:
#	plt.savefig(parmetry['imgfile'])