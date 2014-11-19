#!/usr/bin/python2.7
#  -*- coding: utf-8 -*-
from ownlib.pastanalyzeoneagent import pastanalyzeoneagent
argh = argparse.ArgumentParser()
argh.add_argument('-i', '--interactively', type=TrueOrFalse, help="Interactively (True/False)")
argh.add_argument('-f','--dbfilepath',type=str,help="Specify dabatase file",default='defdb.xml')
argh.add_argument('-y','--dbtype',type=str,help="Specify database type",default='xml',choices=('xml','csv'))
argh.add_argument('-s','--startdatetime',type=between,help="Start date of data to analyze formatted YYYYMMDDHHMMSS",default=20000000000000)
argh.add_argument('-e','--enddatetime',type=between,help="End date of data to analyze formatted YYYYMMDDHHMMSS",default=20000000000000)
argh.add_argument('-n','--codename',type=str,help="Enter codename (soon you will be able to use ut multiple times")
#TODO: multiple codenames — multiple Agents to be analyzed
if parmetry['dbtype'] == 'xml':
	if int(parmetry['startdatetime']) > 20000000000000:
		strd = str(parmetry['datetime'])
		dy = strd[0]+strd[1]+strd[2]+strd[3]
		dm = strd[4]+strd[5]
		dd = strd[6]+strd[7]
		dh = strd[8]+strd[9]
		di = strd[10]+strd[11]
		ds = strd[12]+strd[13]
		import calendar
		tup = (int(dy),int(dm),int(dd),int(dh),int(di),int(ds))
		stimed = calendar.timegm(tup)
	if int(parmetry['enddatetime']) > 20000000000000:
		strd = str(parmetry['datetime'])
		dy = strd[0]+strd[1]+strd[2]+strd[3]
		dm = strd[4]+strd[5]
		dd = strd[6]+strd[7]
		dh = strd[8]+strd[9]
		di = strd[10]+strd[11]
		ds = strd[12]+strd[13]
		import calendar
		tup = (int(dy),int(dm),int(dd),int(dh),int(di),int(ds))
		etimed = calendar.timegm(tup)
	elif int(parmetry['enddatetime']) == 20000000000000:
		etimed = time.time()
	if int(parmetry['startdatetime']) == 20000000000000:
		from datetime import datetime
		from dateutil.relativedelta import relativedelta
		eda = datetime.utcfromtimestamp(etimed)
		ede = eda - relativedelta(months=6)
		stimed = int(ede.strftime("%s"))



print "Hello World, this program can import the pastanalyzeoneagent"
pastanalyzeoneagent(codename)