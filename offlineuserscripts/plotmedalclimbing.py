#!/usr/bin/python2.7
#  -*- coding: utf-8 -*-
import argparse
from ..ownlib.pastanalyzeoneagent import pastanalyzeoneagent

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
arug = argh.add_mutually_exclusive_group()
arug.add_argument('-mb','--bronze',action='store_true',help="Show the chart for bronze-aspiring medals")
arug.add_argument('-ms','--silver',action='store_true',help="Show the chart for silver-aspiring medals")
arug.add_argument('-mg','--gold',action='store_true',help="Show the chart for gold-aspiring medals")
arug.add_argument('-mp','--platinum',action='store_true',help="Show the chart for platinum-aspiring medals")
arug.add_argument('-mo','--onyx',action='store_true',help="Show the chart for onyx-aspiring medals")


parmetry = vars(argh.parse_args())

codename = parmetry['codename']

if parmetry['dbfilepath']:
	pa = pastanalyzeoneagent(codename,filepath=str(parmetry['dbfilepath']))
else:
	pa = pastanalyzeoneagent(codename)

from ..ownlib.clarifydata import clarifydata
clar = clarifydata()
from ..ownlib.gameinfo import gameinfo
ginf = gameinfo()
clrs = clar.colorsqua
dor = pa.medalclimbing()
jestcoler = False
for coltry in ('bronze','silver','gold','platinum','onyx'):
	if parmetry[coltry]:
		coler = coltry
		jestcoler = True
		break
if not jestcoler:
	from ownlib.singleentry import singleentry
	sing = singleentry()
	curen = pa.givemenewestcurrent()
	bap = sing.calclvlbyap(int(curen['ap']))
	ounce = sing.calcrealcountofmedalsonce(curen,cur=curen,what='currentbutstr')
	once = {}
	for i in ounce.keys():
		once[i] = int(ounce[i])
	mult = sing.calcsomecountofmedalsmulti(once)
	bmed = min(sing.calclvlbycol(mult).values())
	lewel = sing.calcreallvl(bap,bmed)
	reqmed = ginf.reqmed(lewel)
	for i in reqmed.keys():
		if reqmed[i] > int(curen[i]):
			coler = i
			jestcoler = True
			break
barck = pa.propmedalclimbingrelative(dor,coler)
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
fig=plt.figure(figsize=(12,10))
ax = fig.add_subplot(111)
ax.set_position([0.05,0.05,0.8,0.9])
for i in back.keys():
	plotting[i] = ax.plot(back[i][0],back[i][1],color=dictclrs[i],linewidth=2.0,label=ginf.medaldict[i if i != 'guardnow' else 'guard']['name'])
from matplotlib.font_manager import FontProperties
fontP = FontProperties()
fontP.set_size('small')
ax.legend(bbox_to_anchor=(1.0, 0.5), fancybox=True, shadow=True, loc='center left', ncol=1, prop=fontP)
plt.axis([min(pa.givemetimes()),max(pa.givemetimes()),0,1])
plt.title('Medals aspiring to %s' % coler)
plt.ylabel('Percent of %s medal' % coler)
def dtformater(x,pos): from datetime import datetime; return datetime.utcfromtimestamp(int(x)).isoformat(sep='\n')
def percformater(x,pos): return '%2.f%%' % (x*100)
ax.yaxis.set_major_formatter(FuncFormatter(percformater))
ax.xaxis.set_major_formatter(FuncFormatter(dtformater))
#if not parmetry['nogui']:
plt.show()
#if parmetry['writeimg']:
#	plt.savefig(parmetry['imgfile'])