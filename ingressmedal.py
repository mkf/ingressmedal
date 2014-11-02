#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import argparse

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
			if (range(0,99999).index(int(ciag)) > 0):
				return int(ciag)
			elif (range(0,99999).index(int(ciag)) == 0):
				return int(ciag)
		except:
			raise argparse.ArgumentTypeError('It is not "n" nor a number. Although it had to.')

argh = argparse.ArgumentParser()
from interactive import interactive
interaktywnosciowo = interactive()
for keyowo in interaktywnosciowo.gimmecurrentquestionsuredict().keys():
	argh.add_argument(('-'+keyowo), ('--'+keyowo), type=int, help=(interaktywnosciowo.gimmecurrentquestionsuredict()[keyowo]))
	print keyowo #debug
for keyowko in interaktywnosciowo.gimmecurrentquestionunsuredict().keys():
	argh.add_argument(('-'+keyowko), ('--'+keyowko), type=BigNumberORn, help=(interaktywnosciowo.gimmecurrentquestionunsuredict()[keyowko]))
	print keyowko #debug
argh.add_argument('-i', '--interactively', type=TrueOrFalse, help="Interactively")
parmetry = vars(argh.parse_args())


class current:
	"This class applies only to current stats, it doesn't compare anything to the past"
	def __init__(self,codename,interactively,current):
		self.current = current
		from interactive import interactive
		interaktywnosc = interactive()
		self.interaktywnosc = interaktywnosc
		if interactively == False:
			for kluczykoa in interaktywnosc.gimmecurrentquestionsuredict().keys():
				try:
					bzdurkaldkfh = str(self.current[kluczykoa])
				except:
					print "Interactively is False. There is no %s, exiting." % kluczykoa
					quit()
			for kluczykoa in interaktywnosc.gimmecurrentquestionunsuredict().keys():
				try:
					bzdurkafdhgljsdk = str(self.current[kluczykoa])
				except:
					print "Interactively is False. There is no %s, exiting. Next time put in at least an 'n' character." % kluczykoa
					quit()
		elif interactively == True:
			kluczykoal = []
			for kluczykoa in interaktywnosc.gimmecurrentquestionsuredict().keys():
				try:
					bzdurkaldkfh = str(self.current[kluczykoa])
				except:
					kluczykoal.append(kluczykoa)
			for kluczykoa in interaktywnosc.gimmecurrentquestionunsuredict().keys():
				try:
					bzdurkafdhgljsdk = str(self.current[kluczykoa])
				except:
					kluczykoal.append(kluczykoa)
			kluczbejs = (interaktywnosc.gimmecurrentquestionsuredict().keys() + interaktywnosc.gimmecurrentquestionunsuredict().keys()).sort()
			kluczvs = kluczykoal.sort()
			if kluczbejs == kluczvs:
				interaktywnosc.current()
			else:
				try:
					for kluczykob in kluczykoal:
						self.current[kluczykob] = interaktywnosc.currentwyrywki(kluczykob)
				except:
					dkfjlghfflfsdhg = "dflgh"
		else:
			print "Interactively can't be: "
			try:
				print interactively
			except:
				print "<unreadable>"
			print "   because such value is unsuitable for the situation."
			print "Exiting"
			quit()
	def rjeturncount(self):
		return self.current
	def coUNTINGcurapcountable(self):
			current = self.current
			curapcountable = {
				'seer': (current['seer']*1000),
				'depllater': ((current['depl']-current['capt'])*125),
				'link': (current['link']*313),
				'field': (current['field']*1250),
				'rechmin': (current['rech']*10),
				'captres': (current['capt']*625),
				'destr': (current['destr']*75),
				'destrlink': (current['destrlink']*187),
				'destrfield': (current['destrfield']*750),
			}
			if current['photo'] == 'n':
				print "That's your fault you don't know how much AP you've gained on photos."
			else:
				curapcountable['photo'] = (current['photo']*500)
			if current['edit'] == 'n':
				print "That's your fault you don't know how much AP you've gained on edits."
			else:
				curapcountable['edit'] = (current['edit']*200)
			return curapcountable
	def percent(self):
			things = self.coUNTINGcurapcountable()
			for w in sorted(things, key=things.get, reverse=True):
				print w, things[w]

interactively = parmetry['interactively']
hello = current('ArchieT', interactively,parmetry)
hello.coUNTINGcurapcountable()