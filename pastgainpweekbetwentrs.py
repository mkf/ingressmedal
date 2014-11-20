#!/usr/bin/python2.7
#  -*- coding: utf-8 -*-
from ownlib.pastanalyzeoneagent import pastanalyzeoneagent
import argparse
def TrueOrFalse(ciag):
	if (ciag == "True") or (ciag == "y") or (ciag == "yes"):
		return True
	elif (ciag == "False") or (ciag == "n") or (ciag == "no"):
		return False
	else:
		raise argparse.ArgumentTypeError('It is not True nor False, y nor n, yes nor no. Although it had to.')
def between(ciag):
	if 20000000000000 < int(ciag) < 22000000000000:
		return int(ciag)
	else:
		raise argparse.ArgumentTypeError('It is a wrong date')
argh = argparse.ArgumentParser()
argh.add_argument('-i', '--interactively', type=TrueOrFalse, help="Interactively (True/False)",choices=(True,False))
argh.add_argument('-o', '--overs', type=TrueOrFalse, help="Show overs (True/False)",choices=(True,False))
argh.add_argument('-f','--dbfilepath',type=str,help="Specify dabatase file",default='defdb.xml')
argh.add_argument('-y','--dbtype',type=str,help="Specify database type",default='xml',choices=('xml','csv'))
argh.add_argument('-s','--startdatetime',type=between,help="Start date of data to analyze formatted YYYYMMDDHHMMSS",default=20000000000000)
argh.add_argument('-e','--enddatetime',type=between,help="End date of data to analyze formatted YYYYMMDDHHMMSS",default=20000000000000)
argh.add_argument('-n','--codename',type=str,help="Enter codename (soon you will be able to use ut multiple times",required=True)
argh.add_argument('-v','--vertically',type=TrueOrFalse,help="Show the table vertically True(default)/False",choices=(True,False),default=True)
#TODO: multiple codenames — multiple Agents to be analyzed
parmetry = vars(argh.parse_args())
if parmetry['dbtype'] == 'xml':
	if int(parmetry['startdatetime']) > 20000000000000:
		strd = str(parmetry['datetime'])
		dy = strd[0]+strd[1]+strd[2]+strd[3]
		dm = strd[4]+strd[5]
		dd = strd[6]+strd[7]
		dh = strd[8]+strd[9]
		di = strd[10]+strd[11]
		ds = strd[12]+strd[13]
		import calendar
		tup = (int(dy),int(dm),int(dd),int(dh),int(di),int(ds))
		stimed = calendar.timegm(tup)
	if int(parmetry['enddatetime']) > 20000000000000:
		strd = str(parmetry['datetime'])
		dy = strd[0]+strd[1]+strd[2]+strd[3]
		dm = strd[4]+strd[5]
		dd = strd[6]+strd[7]
		dh = strd[8]+strd[9]
		di = strd[10]+strd[11]
		ds = strd[12]+strd[13]
		import calendar
		tup = (int(dy),int(dm),int(dd),int(dh),int(di),int(ds))
		etimed = calendar.timegm(tup)
	elif int(parmetry['enddatetime']) == 20000000000000:
		import time
		etimed = time.time()
	if int(parmetry['startdatetime']) == 20000000000000:
		from datetime import datetime
		from dateutil.relativedelta import relativedelta
		eda = datetime.utcfromtimestamp(etimed)
		ede = eda - relativedelta(months=6)
		stimed = int(ede.strftime("%s"))

if parmetry['interactively'] == 'None' or parmetry['interactively'] is None:
	interactively = True
else:
	interactively = parmetry['interactively']

if parmetry['overs'] == 'None' or parmetry['overs'] is None:
	overs = False
else:
	overs = parmetry['overs']

codename = parmetry['codename']

if parmetry['dbfilepath'] and overs:
	pa = pastanalyzeoneagent(codename,filepath=str(parmetry['dbfilepath']),overs=overs)
elif parmetry['dbfilepath']:
	pa = pastanalyzeoneagent(codename,filepath=str(parmetry['dbfilepath']))
elif overs:
	pa = pastanalyzeoneagent(codename,overs=overs)
else:
	pa = pastanalyzeoneagent(codename)

from ownlib.clarifydata import clarifydata
clar = clarifydata()
head = clar.AskForTheListOfDataToBeSavedFromCurrent
entries = {}

for entr in pa.gainbetweenentries('uniqvis')['d'].keys():
	entries[entr] = {}

dpti = {}

for param in head:
	gain = pa.gainbetweenentries(param)
	dpti[param] = {}
	pert = pa.gainpertime(gain['d'],gain['f'])
	for ent in entries.keys():
		entries[ent][param] = pert[ent]

tabel = []
for entry in entries.keys():
	subt = []
	for par in head:
		subt.append(float(float(entries[entry][par])*float(60*60*24*7)))
	tabel.append(subt)
if not parmetry['vertically']:
	from tabulate import tabulate
	aut = tabulate(tabel,headers=head,floatfmt=".4f")
elif parmetry['vertically']:
	vert = []
	for i in head:
		ind = head.index(i)
		vert.append([i])
		for a in tabel:
			vert[ind].append(a[ind])

	from tabulate import tabulate
	aut = tabulate(vert,floatfmt=".4f")
print " "
print " "
print aut