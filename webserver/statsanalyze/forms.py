# -*- coding: utf-8 -*-
__author__ = 'ArchieT'
from django import forms
from .models import Entry

#TODO: OCR
#class EntryOCRform(forms.ModelForm):
#	class Meta:
#		model = Entry
#		fields = ()

class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = (
			'timepart',
			'agentdb',
			'public',
			'entry_date',
			'ap',
			'bronze',
			'silver',
			'gold',
			'platinum',
			'onyx',
			'nomedal',
			'uniqvis',
			'seer',
			'xm',
			'walk',
			'depl',
			'link',
			'field',
			'allfieldmusum',
			'longestlink',
			'largestfield',
			'rech',
			'capt',
			'uniqcapt',
			'mods',
			'destr',
			'neutr',
			'destrlink',
			'destrfield',
			'guard',
			'guardlink',
			'maxlinklenxdays',
			'guardfield',
			'maxfieldmuxdays',
			'hack',
			'edits',
			'photos',
			'recruiter',
		)