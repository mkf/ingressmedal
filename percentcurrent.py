#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import argparse
from Current import Current


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


argh = argparse.ArgumentParser()
from interactive import Interactive

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