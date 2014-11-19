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
			'ap': ('ap'),
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
			)
			'notmedalbutap': ('destrlink','destrfield','photo','edit')
		}

		#colorbrewer2.org, qualitative, 12 data classes
		self.colorsqua = (
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

	@property
	def AskForTheListOfDataToBeSavedFromCurrent(self):
		return self.listofdatatobesavedfromcurrent