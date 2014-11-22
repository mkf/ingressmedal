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
			'uniqvis':r'Un[il]qu[eP] Por[tf]als [Vv][il]s[il][tl][Pe]d ',
			'seer':r'Portals Discovered ',
			'xm':r'XM Coll[eP][cI][tI][eP]d ',
			'hack':r'Ha[cI]ks ',
			'depl':r'R[eP]sona[tl]ors D[eP]ploy[eP]d ',
			'link':r'L[il]nks Cr[eP]a[tl][eP]d ',
			'field':r'Con[tl]rol F[iI][eP]lds Cr[eP]a[tl][eP]d ',
			'mu':r'M[il]nd Un[il][tl]s Cap[tl]ur[eP]d ',
			'longestlink':r'Long[eP]s[tl] L[il]nk Ev[eP]r Cr[eP]a[tl][eP]d ',
			'largestfield':r'Larg[eP]s[tl] Con[tl]rol F[iI][eP]ld ',
			'rech':r'XM R[eP][cI]harg[eP]d ',
			'capt':r'^Por[tlf]als Cap[tl]ur[eP]d ',
			'uniqcapt':r'Un[il]qu[eP] Por[tlf]als Cap[tl]ur[eP]d ',
			'destr':r'R[eP]sona[tl]ors D[eP]s[tl]roy[eP]d ',
			'neutr':r'Por[tf]als N[eP]u[tl]ral[il][zI_][eP]d ', #'Porlals NPulrall_Pd IBT'
			'destrlink':r'En[eP]my L[il]nks D[eP]s[tl]roy[eP]d ',
			'destrfield':r'En[eP]my Con[tl]rol F[iI][eP]lds D[eP]s[tl]roy[eP]d ',
			'walk':r'D[il]s[tl]a[nm]*[cm]*[eP] Walk[eP]d ',
			'guard':r'Max T[il]m[eP] Por[tf]al H[eP]ld ',
			'guardlink':r'Max T[il]m[eP] L[il]nk Ma[il]n[tl]a[il]n[eP]d ',
			'longxguardlink':r'Max L[il]nk L[eP]ng[tl]h x Days ',
			'guardfield':r'Max T[il]m[eP] Fi[eP]ld H[eP]ld ',
			'longxguardfield':r'Larg[eP]s[tl] F[iI][eP]ld MUs x Days '
		}
		self.origstrsdictaft = {
			'ap':r' A[Pp] .+A[Pp]',
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
		}
		#self.sortedbypositionwithheaders = (
		#
		#)
		#self.sortedheadersbypositionwithrecur = (
		#
		#)