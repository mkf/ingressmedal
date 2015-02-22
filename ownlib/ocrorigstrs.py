# -*- coding: utf-8 -*-
class ocrorigstrs:
	def __init__(self, czasowe=True):
		self.sortedbyposition = (
			'ap',
			'uniqvis',
			'seer',
			'xm',
			'walk',
			'depl',
			'link',
			'field',
			'mu',
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
			'longxguardlink',
			'guardfield',
			'longxguardfield',
			'uniqmis',
			'hack',
			'glyph',
		) if czasowe else ('linksactiv','pwned','fieldsactiv','mucontrol')
		self.origstrsdictbef = {
			'ap':r'^[_-]{0,3} ?',
			'uniqvis':r'Un[il]qu[eP] Por[tf]als [Vv][il]s[il][tl][Pe]d ',
			'seer':r'Por[tf]als [DO][il]s[cI]ov[eP]r[eP]d ',   #'Porfals OlsIovPrPd l'
			'xm':r'XM Coll[eP][cI][tI][eP]d ',
			'hack':r'Ha[cI]ks ',
			'depl':r'R[eP]sona[tl]ors [DO][eP]ploy[eP]d ',
			'link':r'L[il]nks Cr[eP]a[tl][eP]d ',
			'field':r'Con[tl]rol F[iI][eP]lds Cr[eP]a[tl][eP]d ',
			'mu':r'M[il]nd Un[il][tl]s Cap[tl]ur[eP]d ',
			'longestlink':r'Long[eP]s[tl] L[il]nk Ev[eP]r Cr[eP]a[tl][eP]d ',
			'largestfield':r'Larg[eP]s[tl] Con[tl]rol F[iI][eP]ld ',
			'rech':r'XM R[eP][cI]harg[eP]d ',
			'capt':r'^Por[tlf]als Cap[tl]ur[eP]d ',
			'uniqcapt':r'Un[il]qu[eP] Por[tlf]als Cap[tl]ur[eP]d ',
			'destr':r'R[eP]sona[tl]ors [DO][eP]s[tl]roy[eP]d ',
			'neutr':r'Por[tlf]als N[eP]u[tl]ral[il][zI_][eP]d ', #'Porlals NPulrall_Pd IBT'
			'destrlink':r'En[eP]my L[il]nks [DO][eP]s[tl]roy[eP]d ',
			'destrfield':r'En[eP]my Con[tl]rol F[iI][eP]lds [DO][eP]s[tl]roy[eP]d ',
			'walk':r'[DO][il]s[tl]a[nm]*[cm]*[eP] Walk[eP]d ',   #'OlslamP WalkPd 9km'
			'guard':r'Max T[il]m[eP] Por[tlf]al H[eP]ld ',  #'Max TlmP Porlal HPld 14 day5'
			'guardlink':r'Max T[il]m[eP] L[il]nk Ma[il]n[tl]a[il]n[eP]d ',
			'longxguardlink':r'Max L[il]nk L[eP]ng[tl]h x [DO]ays ',
			'guardfield':r'Max T[il]m[eP] Fi[eP]ld H[eP]ld ',
			'longxguardfield':r'Larg[eP]s[tl] F[iI][eP]ld MUs x [DO]ays ',
			'mods':r'Mods [DO][il]s[cI]ov[eP]r[eP]d ',
			'uniqmis':r'Un[il]qu[eP] m[il][sS5][sS5][il]on[sS5] completed ',
			'glyph':r'Glyph Hack Points ',
		} if czasowe else {
			'linksactiv':r'L[il]nks Active ',
			'pwned':r'Por[tlf]als Owned ',
			'fieldsactiv':r'Con[tl]rol F[iI][eP]lds Active ',
			'mucontrol':r'M[il]nd Un[il][tl] Control ',
		}
		self.origstrsdictaft = {
			'ap':r'[ ]?A[Pp][ \|Il_]+.+A[Pp]',
			'xm': r' XM',
			'mu': r'MUs',
			'longestlink':r'km',
			'largestfield':r'MUs',
			'rech':r' XM',
			'walk':r'km',
			'guard':r' day[S5s]',
			'guardlink':r' day[S5s]',
			'longxguardlink':r' km-day[s5]',
			'guardfield':r' days',
			'longxguardfield':r' MU-day[s5]'
		} if czasowe else {'mucontrol':r'MUs'}
		#self.sortedbypositionwithheaders = (
		#
		#)
		#self.sortedheadersbypositionwithrecur = (
		#
		#)