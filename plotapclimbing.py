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

