#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import argparse

from ownlib.Current import Current


def TrueOrFalse(ciag):
	if (ciag == "True") or (ciag == "y") or (ciag == "yes"):
		return True
	elif (ciag == "False") or (ciag == "n") or (ciag == "no"):
		return False
	else:
		raise argparse.ArgumentTypeError('It is not True nor False, y nor n, yes nor no. Although it had to.')


def BigNumberORn(ciag):
	if ciag == 'n':
		return 'n'
	else:
		try:
			if range(0, 99999).index(int(ciag)) > 0:
				return int(ciag)
			elif range(0, 99999).index(int(ciag)) == 0:
				return int(ciag)
		except:
			raise argparse.ArgumentTypeError('It is not "n" nor a number. Although it had to.')

def between(ciag):
	if 20000000000000 < int(ciag) < 22000000000000:
		return int(ciag)
	else:
		raise argparse.ArgumentTypeError('It is a wrong date')


argh = argparse.ArgumentParser()
from ownlib.interactive import Interactive

interaktywnosciowo = Interactive()
argumentydodane = []
for keyowo in interaktywnosciowo.GivMeCurQSdict().keys():
	argh.add_argument(
		('-' + keyowo),
		('--' + keyowo),
		type=int,
		help=(interaktywnosciowo.GivMeCurQSdict()[keyowo]))
	argumentydodane.append(keyowo)
for keyowko in interaktywnosciowo.GivMeCurQUSdict().keys():
	argh.add_argument(
		('-' + keyowko),
		('--' + keyowko),
		type=BigNumberORn,
		help=(interaktywnosciowo.GivMeCurQUSdict()[keyowko]))
	argumentydodane.append(keyowo)
argh.add_argument('-i', '--interactively', type=TrueOrFalse, help="Interactively (True/False)")
argh.add_argument('-o', '--overs', type=TrueOrFalse, help="Show overs (True/False)")
argh.add_argument('-b','--writetodb',action='store_true',help="Append an entry to the database")
argh.add_argument('-f','--dbfilepath',type=str,help="Specify dabatase file",default='defdb.xml')
argh.add_argument('-y','--dbtype',type=str,help="Specify database type",default='xml',choices=('xml','csv'))
argh.add_argument('-d','--datetime',type=between,help="Date of stats formatted YYYYMMDDHHMMSS")
parmetry = vars(argh.parse_args())

if parmetry['interactively'] == 'None' or parmetry['interactively'] is None:
	interactively = True
else:
	interactively = parmetry['interactively']

if parmetry['overs'] == 'None' or parmetry['overs'] is None:
	overs = False
else:
	overs = parmetry['overs']
curinst = Current('ArchieT', interactively, parmetry, argumentydodane, overs)
curinst.percentofap()
curinst.percentofdest()
if parmetry['writetodb']:
	if parmetry['dbtype'] == 'xml':
		if int(parmetry['datetime']) > 20000000000000:
			strd = str(parmetry['datetime'])
			dy = strd[0]+strd[1]+strd[2]+strd[3]
			dm = strd[4]+strd[5]
			dd = strd[6]+strd[7]
			dh = strd[8]+strd[9]
			di = strd[10]+strd[11]
			ds = strd[12]+strd[13]
			import calendar
			tup = (int(dy),int(dm),int(dd),int(dh),int(di),int(ds))
			timed = calendar.timegm(tup)
			curinst.savetoxml(parmetry['dbfilepath'],timed)
			print " "
			print " "
			print "Entry saved to %s" % parmetry['dbfilepath']