# -*- coding: utf-8 -*-
class ocrorigstrs:
	def __init__(self):
		self.sortedbyposition = (
			'ap',
			'uniqvis',
			'seer',
			'xm',
			'hack',
			'depl',
			'link',
			'field',
			'mu',
			'longestlink',
			'largestfield',
			'rech',
			'capt',
			'uniqcapt',
			'destr',
			'neutr',
			'destrlink',
			'destrfield',
			'walk',
			'guard',
			'guardlink',
			'longxguardlink',
			'guardfield',
			'longxguardfield'
		)
		self.origstrsdictbef = {
			'ap':r'^[_-]{0,3} ?',
			'uniqvis':r'Unique Portals Visited ',
			'seer':r'Portals Discovered ',
			'xm':r'XM Collected ',
			'hack':r'Hacks ',
			'depl':r'Resonators Deployed ',
			'link':r'Links Created ',
			'field':r'Control Fields Created ',
			'mu':r'Mind Units Captured ',
			'longestlink':r'Longest Link Ever Created ',
			'largestfield':r'Largest Control Field ',
			'rech':r'XM Recharged ',
			'capt':r'^Portals Captured ',
			'uniqcapt':r'Unique Portals Captured ',
			'destr':r'Resonators Destroyed ',
			'neutr':r'Portals Neutralized ',
			'destrlink':r'Enemy Links Destroyed ',
			'destrfield':r'Enemy Control Fields Destroyed ',
			'walk':r'Distance Walked ',
			'guard':r'Max Time Portal Held ',
			'guardlink':r'Max Time Link Maintained ',
			'longxguardlink':r'Max Link Length x Days ',
			'guardfield':r'Max Time Field Held ',
			'longxguardfield':r'Largest Field MUs x Days '
		}
		self.origstrsdictaft = {
			'ap':r' A[Pp] .+A[Pp]',
			'xm': r' XM',
			'mu': r'MUs',
			'longestlink':r'km',
			'largestfield':r'MUs',
			'rech':r' XM',
			'walk':r'km',
			'guard':r' days',
			'guardlink':r' days',
			'longxguardlink':r' km-days',
			'guardfield':r' days',
			'longxguardfield':r' MU-days'
		}
		#self.sortedbypositionwithheaders = (
		#
		#)
		#self.sortedheadersbypositionwithrecur = (
		#
		#)