# -*- coding: utf-8 -*-

class clarifydata:
	def __init__(self):
		self.listofdatatobesavedfromcurrent = (
			'ap',
			'bronze',
			'silver',
			'gold',
			'platinum',
			'onyx',
			'uniqvis',
			'seer',
			'hack',
			'depl',
			'link',
			'field',
			'rech',
			'capt',
			'uniqcapt',
			'destr',
			'guard',
			'guardnow',
			'destrlink',
			'destrfield',
			'photo',
			'edit',
		)

		self.thesavelistgrouped = {
			'ap': tuple(['ap']),
			'medalcolors': ('bronze','silver','gold','platinum','onyx'),
			'medalthings': (
				'uniqvis',
				'seer',
				'hack',
				'depl',
				'link',
				'field',
				'rech',
				'capt',
				'uniqcapt',
				'destr',
				'guard',
				'guardnow',
			),
			'notmedalbutap': ('destrlink','destrfield','photo','edit')
		}

		self.colorsqua = self.colorsonwhite

		#colorbrewer2.org, qualitative, 12 data classes
		self.colorsqualitative = (
			'#A6CEE3',
			'#1F78B4',
			'#B2DF8A',
			'#33A02C',
			'#FB9A99',
			'#E31A1C',
			'#FDBF6F',
			'#FF7F00',
			'#CAB2D6',
			'#6A3D9A',
			'#FFFF99',
			'#B15928'
		)

		self.colorsonwhite = (
			'#000000',
			'#FF0000',
			'#0000FF',
			'#FFEE00',
			'#00CCFF',
			'#FF00FF',
			'#9E9E9E',
			'#FFAA00',
			'#0489B1',
			'#AA5500',
			'#00AA7F',
			'#00CC00'
		)

	@property
	def AskForTheListOfDataToBeSavedFromCurrent(self):
		return self.listofdatatobesavedfromcurrent