#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ownlib.OcrRead import OcrRead
import argparse
argh = argparse.ArgumentParser()
argh.add_argument('-p','--fromimage',type=str,help="Specify image file",required=True)
argh.add_argument('-c','--cache',type=str,help="Specify .pbm image cache file",default='cache.pbm')




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
argh.add_argument('-w','--writetodb',action='store_true',help="Append an entry to the database")
argh.add_argument('-f','--dbfilepath',type=str,help="Specify dabatase file",default='defdb.xml')
argh.add_argument('-y','--dbtype',type=str,help="Specify database type",default='xml',choices=('xml','csv'))
argh.add_argument('-d','--datetime',type=between,help="Date of stats formatted YYYYMMDDHHMMSS")
argh.add_argument('-n','--codename',type=str,help="Agent's codename",required=True)


parmetry = vars(argh.parse_args())
o = OcrRead()
e = o.ocrad_get(parmetry['fromimage'],parmetry['cache'])
fin = o.ocradalterproc(e)

if not parmetry['datetime']:
	import re
	dejta = re.search(r'profile_20\d\d\d\d\d\d_\d\d\d\d\d\d',parmetry['fromimage'])
	dtfromfilename = re.sub('_','',re.sub('profile_','',dejta.string)) if dejta is not None else False


if parmetry['writetodb'] and not parmetry['datetime'] and not dtfromfilename:
	print "Argument '-d YYMMDDHHMMSS' or date-containing image filename required if you want to write to db. See --help for more information"
	quit()

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
			strd = str(parmetry['datetime'] or dtfromfilename)
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
else:
	print " "
	print " "
	print "WARNING: Data were not saved - use -w parameter"
	print " "
	print " "