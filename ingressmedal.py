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
			if range(0, 99999).index(int(ciag)) > 0:
				return int(ciag)
			elif range(0, 99999).index(int(ciag)) == 0:
				return int(ciag)
		except:
			raise argparse.ArgumentTypeError('It is not "n" nor a number. Although it had to.')


argh = argparse.ArgumentParser()
from interactive import interactive

interaktywnosciowo = interactive()
for keyowo in interaktywnosciowo.gimmecurrentquestionsuredict().keys():
	argh.add_argument(
		('-' + keyowo),
		('--' + keyowo),
		type=int,
		help=(interaktywnosciowo.gimmecurrentquestionsuredict()[keyowo]))
for keyowko in interaktywnosciowo.gimmecurrentquestionunsuredict().keys():
	argh.add_argument(
		('-' + keyowko),
		('--' + keyowko),
		type=BigNumberORn,
		help=(interaktywnosciowo.gimmecurrentquestionunsuredict()[keyowko]))
argh.add_argument('-i', '--interactively', type=TrueOrFalse, help="Interactively")
parmetry = vars(argh.parse_args())


class current:
	"""This class applies only to current stats, it doesn't compare anything to the past"""

	def __init__(self, codename, interactively, current):
		from interactive import interactive

		interaktywnosc = interactive()
		self.interaktywnosc = interaktywnosc
		if interactively == False:
			for kluczykoa in interaktywnosc.gimmecurrentquestionsuredict().keys():
				try:
					bzdurkaldkfh = str(current[kluczykoa])
					if bzdurkaldkfh == None or bzdurkaldkfh == "None":
						print "Interactively is False. There is no %s, exiting." % kluczykoa
						quit()
				except:
					print "Interactively is False. There is no %s, exiting." % kluczykoa
					quit()
			for kluczykoa in interaktywnosc.gimmecurrentquestionunsuredict().keys():
				try:
					bzdurkafdhgljsdk = str(current[kluczykoa])
					if bzdurkafdhgljsdk == None or bzdurkafdhgljsdk == "None":
						print "Interactively is False. There is no %s, exiting." % kluczykoa
						quit()

				except:
					print "Interactively is False. There is no %s, exiting. Next time put in at least an 'n' character." % kluczykoa
					quit()
		elif interactively == True:
			kluczykoal = []
			# print interaktywnosc.gimmecurrentquestionsuredict().keys() #debug
			# print interaktywnosc.gimmecurrentquestionunsuredict().keys() #debug
			for kluczykoa in interaktywnosc.gimmecurrentquestionsuredict().keys():
				# print kluczykoa #debug
				# Why it doesn't append the kluczykoa at the kluczykoal??
				try:
					bzdurkaldkfh = str(current[kluczykoa])
					# print "jesttraj" #debug
					# print bzdurkaldkfh #debug
					# print "----------------" #debug
					if bzdurkaldkfh == None or bzdurkaldkfh == "None" or self.CzyLiczbaZeroDoPiecDziewiatek(
							bzdurkaldkfh) == False:
						kluczykoal.append(str(kluczykoa))
					# print "jestnolnem" #debug
				except:
					kluczykoal.append(str(kluczykoa))
				# print "niema" #debug
			for kluczykoa in interaktywnosc.gimmecurrentquestionunsuredict().keys():
				# print kluczykoa #debug
				# Why it doesn't append the kluczykoa at the kluczykoal??
				try:
					bzdurkafdhgljsdk = str(current[kluczykoa])
					# print "jestTrajProba" #debug
					# print bzdurkafdhgljsdk #debug
					# print "--------" #debug
					if bzdurkafdhgljsdk == None or bzdurkafdhgljsdk == "None" or self.CzyLiczbaZeroDoPiecDziewiatekLUBn(
							bzdurkafdhgljsdk) == False:
						kluczykoal.append(str(kluczykoa))
					# print "jestNolnem" #debug
				except:
					kluczykoal.append(str(kluczykoa))
				# print "NiMa" #debug
			#kluczbejs = (interaktywnosc.gimmecurrentquestionsuredict().keys() + interaktywnosc.gimmecurrentquestionunsuredict().keys()).sort()
			kluczbejs = []
			kluczbejs.extend(interaktywnosc.gimmecurrentquestionsuredict().keys())
			kluczbejs.extend(interaktywnosc.gimmecurrentquestionunsuredict().keys())
			kluczbejs.sort()
			kluczvs = kluczykoal.sort()
			# print "kluczbejs" #debug
			# print kluczbejs #debug
			# print "kluczvs" #debug
			# print kluczvs #debug
			# print "kluczykoal" #debug
			# print kluczykoal #debug
			if kluczbejs == kluczvs:
				interaktywnosc.current()
			else:
				# if True:
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
		self.current = current

	def rjeturncount(self):
		return self.current

	def TrueczyFalse(self, ciag):
		if ((str(ciag == "True")) or (ciag == "y") or (ciag == "yes")) or (
						(ciag == "False") or (ciag == "n") or (ciag == "no")):
			return True
		else:
			return False

	def CzyLiczbaZeroDoPiecDziewiatek(self, ciag):
		if (range(0, 99999).index(int(ciag)) > 0) or (range(0, 99999).index(int(ciag)) == 0):
			return True
		else:
			return False

	def CzyLiczbaZeroDoPiecDziewiatekLUBn(self, ciag):
		if (range(0, 99999).index(int(ciag)) > 0) or (range(0, 99999).index(int(ciag)) == 0) or (str(ciag) == 'n'):
			return True
		else:
			return False

	def coUNTINGcurapcountable(self):
		current = self.current
		curapcountable = {
			'seer': (current['seer'] * 1000),
			'depllater': ((current['depl'] - current['capt']) * 125),
			'link': (current['link'] * 313),
			'field': (current['field'] * 1250),
			'rechmin': (current['rech'] * 10),
			'captres': (current['capt'] * 625),
			'destr': (current['destr'] * 75),
			'destrlink': (current['destrlink'] * 187),
			'destrfield': (current['destrfield'] * 750),
		}
		if current['photo'] == 'n':
			print "That's your fault you don't know how much AP you've gained on photos."
		else:
			curapcountable['photo'] = (current['photo'] * 500)
		if current['edit'] == 'n':
			print "That's your fault you don't know how much AP you've gained on edits."
		else:
			curapcountable['edit'] = (current['edit'] * 200)
		return curapcountable

	def percent(self):
		things = self.coUNTINGcurapcountable()
		for w in sorted(things, key=things.get, reverse=True):
			print w, things[w]


if parmetry['interactively'] == 'None':
	interactively = True
elif parmetry['interactively'] == None:
	interactively = True
else:
	interactively = parmetry['interactively']
hello = current('ArchieT', interactively, parmetry)
hello.coUNTINGcurapcountable()