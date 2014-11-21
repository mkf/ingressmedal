# -*- coding: utf-8 -*-
class gameinfo:
	def __init__(self):
		self.medaldict = {
			'uniqvis': {'name': 'Explorer', 'sdesc': 'Uniq visited', 'apable': False,
						'walk': {'bronze': 100, 'silver': 1000, 'gold': 2000, 'platinum': 10000, 'onyx': 30000},
						'over': 'hack', 'sub': False},
			'seer': {'name': 'Seer', 'sdesc': 'Portals discovered', 'apable': True,
					 'walk': {'bronze': 10, 'silver': 20, 'gold': 200, 'platinum': 500, 'onyx': 5000}, 'over': False,
					 'sub': False},
			'hack': {'name': 'Hacker', 'sdesc': 'Hacks', 'apable': False,
					 'walk': {'bronze': 2000, 'silver': 10000, 'gold': 30000, 'platinum': 100000, 'onyx': 200000},
					 'over': False, 'sub': 'uniqvis'},
			'depl': {'name': 'Builder', 'sdesc': 'Resonators deployed', 'apable': True,
					 'walk': {'bronze': 2000, 'silver': 10000, 'gold': 30000, 'platinum': 100000, 'onyx': 200000},
					 'over': False, 'sub': 'capt'},
			'link': {'name': 'Connector', 'sdesc': 'Links created', 'apable': True,
					 'walk': {'bronze': 50, 'silver': 1000, 'gold': 5000, 'platinum': 25000, 'onyx': 100000},
					 'over': False,
					 'sub': 'field'},
			'field': {'name': 'Mind Controller', 'sdesc': 'CFields created', 'apable': True,
					  'walk': {'bronze': 100, 'silver': 500, 'gold': 2000, 'platinum': 10000, 'onyx': 40000},
					  'over': 'link', 'sub': False},
			'rech': {'name': 'Recharger', 'sdesc': 'XM Recharged', 'apable': True,
					 'walk': {'bronze': 100000, 'silver': 1000000, 'gold': 3000000, 'platinum': 10000000,
							  'onyx': 25000000},
					 'over': False, 'sub': False},
			'capt': {'name': 'Liberator', 'sdesc': 'Portals captured', 'apable': True,
					 'walk': {'bronze': 100, 'silver': 1000, 'gold': 5000, 'platinum': 15000, 'onyx': 40000},
					 'over': 'depl', 'sub': 'uniqcapt'},
			'uniqcapt': {'name': 'Pioneer', 'sdesc': 'Uniq captured', 'apable': True,
						 'walk': {'bronze': 20, 'silver': 200, 'gold': 1000, 'platinum': 5000, 'onyx': 20000},
						 'over': 'capt', 'sub': False},
			'destr': {'name': 'Purifier', 'sdesc': 'Resonators destroyed', 'apable': True,
					  'walk': {'bronze': 2000, 'silver': 10000, 'gold': 30000, 'platinum': 100000, 'onyx': 300000},
					  'over': False, 'sub': False},
			'guard': {'name': 'Guardian', 'sdesc': 'Max time portal held', 'apable': False,
					  'walk': {'bronze': 3, 'silver': 10, 'gold': 20, 'platinum': 90, 'onyx': 150}, 'over': False,
					  'sub': False},
		}
		self.lvldict = {
			1: {'ap': 0, 'bene': {'itemy': True, 'xm': 3000, 'rd': 250, 'gamebegun': True}},
			2: {'ap': 2500, 'bene': {'itemy': True, 'xm': 4000, 'rd': 500, 'gamebegun': False}},
			3: {'ap': 20000, 'bene': {'itemy': True, 'xm': 5000, 'rd': 750, 'gamebegun': False}},
			4: {'ap': 70000, 'bene': {'itemy': True, 'xm': 6000, 'rd': 1000, 'gamebegun': False}},
			5: {'ap': 150000, 'bene': {'itemy': True, 'xm': 7000, 'rd': 1250, 'gamebegun': False}},
			6: {'ap': 300000, 'bene': {'itemy': True, 'xm': 8000, 'rd': 1500, 'gamebegun': False}},
			7: {'ap': 600000, 'bene': {'itemy': True, 'xm': 9000, 'rd': 1750, 'gamebegun': False}},
			8: {'ap': 1200000, 'bene': {'itemy': True, 'xm': 10000, 'rd': 2000, 'gamebegun': False}},
			9: {'ap': 2400000, 'silver': 4, 'gold': 1,
				'bene': {'itemy': False, 'xm': 10900, 'rd': 2250, 'gamebegun': False}},
			10: {'ap': 4000000, 'silver': 5, 'gold': 2,
				 'bene': {'itemy': False, 'xm': 11700, 'rd': 2500, 'gamebegun': False}},
			11: {'ap': 6000000, 'silver': 6, 'gold': 5,
				 'bene': {'itemy': False, 'xm': 12400, 'rd': 2750, 'gamebegun': False}},
			12: {'ap': 8400000, 'silver': 7, 'gold': 6,
				 'bene': {'itemy': False, 'xm': 13000, 'rd': 3000, 'gamebegun': False}},
			13: {'ap': 12000000, 'gold': 7, 'platinum': 1,
				 'bene': {'itemy': False, 'xm': 13500, 'rd': 3250, 'gamebegun': False}},
			14: {'ap': 17000000, 'platinum': 2, 'bene': {'itemy': False, 'xm': 13900, 'rd': 3500, 'gamebegun': False}},
			15: {'ap': 24000000, 'platinum': 3, 'bene': {'itemy': False, 'xm': 14200, 'rd': 3750, 'gamebegun': False}},
			16: {'ap': 40000000, 'platinum': 4, 'onyx': 2,
				 'bene': {'itemy': False, 'xm': 14400, 'rd': 4000, 'gamebegun': False}},
		}
		self.highestplaceofnoappearance = {
			'bronze': 8,
			'silver': 8,
			'gold': 8,
			'platinum': 12,
			'onyx': 15
		}
		self.namesforcurapcountable = {'seer': "Portals discovered (submitted)",
									   'depllater': "Sure points from upgrading and deployment of resonators except the capturing res",
									   'link': "Links created", 'field': "Control Fields created",
									   'rechmin': "Minimum AP gained on recharging",
									   'captres': "Capturing portals + first resonator",
									   'destr': "Destroyed resonators", 'destrlink': "Enemy links destroyed",
									   'destrfield': "Enemy Control Fields destroyed",
									   'photo': "Photos added to portals", 'edit': "Edits done to portals' data"}
		self.currentquestionSdict = {
			'ap': 'Current AP: ',
			'uniqvis': 'Current count of unique portals visited: ',
			'seer': 'Current count of discovered portals: ',
			'hack': 'Current count of hacks: ',
			'depl': 'Current count of deployed resonators: ',
			'link': 'Current count of created links: ',
			'field': 'Current count of created Control Fields: ',
			'rech': 'Current count of recharged XM: ',
			'capt': 'Current count captured portals: ',
			'uniqcapt': 'Current count of unique portals captured: ',
			'destr': 'Current count of destroyed resonators: ',
			'guard': 'Current max time portal held in days: ',
			'destrlink': 'Current count of enemy links destroyed: ',
			'destrfield': 'Current count of enemy Control Fields destroyed: ',
			'xm':'Current count of XM collected: ',
			'mu':'Current count of Mind Units captured: ',
			'longestlink':'Currently longst link ever: ',
			'largestfield':'Currently largest field ever: ',
			'neutr':'Current count of neutralized portals: ',
			'walk':'Current distance walked: ',
			'guardlink':'Current max time link maintained: ',
			'guardfield':'Current max time field held: ',
			'longxguardlink':'Current max lenght*time for a link: ',
			'longxguardfield':'Current max MUs*time for a link: '
		}
		self.currentquestionUSdict = {
			'photo': "Current count of photos approved to portals (check mail) (number (even if it's 0) or 'n' character if you don't know): ",
			'edit': "Current count of edits approved to portals (check mail) (number (even if it's 0) or 'n' character if you don't know): ",
			'bronze': "Current count of bronze medals (count only the badges' icons of exactly that color), you may write 'n' if you don't want to write the count: ",
			'silver': "Current count of silver medals (count only the badges' icons of exactly that color), you may write 'n' if you don't need them anymore at your level: ",
			'gold': "Current amount of gold medals (count only the badges' icons of exactly that color), you may write 'n' if you don't need them anymore at your level: ",
			'platinum': "Current amount of platinum medals (count only the badges' icons of exactly that color), you may write 'n' if you don't need them anymore at your level: ",
			'onyx': "Current amount of onyx (black) medals (count only the badges' icons of exactly that color), you may write 'n' if you have the maximum level already: ",
			'guardnow': "Current top max time portal held still alive in days, if you absolutely don't know write an 'n' character: "
		}

	def reqmed(self,lvl):
		colorpossibilities = ('bronze', 'silver', 'gold', 'platinum', 'onyx')
		if True:
			medlvltrytab = []
			for possicolor in colorpossibilities:
				if possicolor in self.lvldict[lvl]:
					if int(self.lvldict[lvl][possicolor]) > 0:
						medlvltrytab.append({possicolor: int(self.lvldict[lvl][possicolor])})
			give = {}
			for a in medlvltrytab:
				give.update(a)
		return give