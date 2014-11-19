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

	@property
	def AskForTheListOfDataToBeSavedFromCurrent(self):
		return self.listofdatatobesavedfromcurrent