#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import wx
import wx.grid
from ownlib.Current import Current

def TrueOrFalse(ciag):
	if (ciag == "True") or (ciag == "y") or (ciag == "yes"):
		return True
	elif (ciag == "False") or (ciag == "n") or (ciag == "no"):
		return False
	else:
		raise ValueError('It is not True nor False, y nor n, yes nor no. Although it had to.')


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
			raise ValueError('It is not "n" nor a number. Although it had to.')



#ID_OPENNEWWNETRYDIALOG = wx.NewId()
#ID_OPENOCRDIALOG = wx.NewId()  #OCR dialog will contain image preview and text fields for each medal colour for manual color recognition, and when it will become automatic, it will show them


from ownlib.interactive import Interactive

interaktywnosciowo = Interactive()
#argumentydodane = []
#for keyowo in interaktywnosciowo.GivMeCurQSdict().keys():
#	argh.add_argument([...]
#		type=int,
#		help=(interaktywnosciowo.GivMeCurQSdict()[keyowo]))
#	argumentydodane.append(keyowo)
#for keyowko in interaktywnosciowo.GivMeCurQUSdict().keys():
#	argh.add_argument([...]
#		type=BigNumberORn,
#		help=(interaktywnosciowo.GivMeCurQUSdict()[keyowko]))
#	argumentydodane.append(keyowo)
#argh.add_argument('-o', '--overs', type=TrueOrFalse, help="Show overs (True/False)")

from ownlib.GUI.NewEntryDialog import NewEntryDialog

from ownlib.GUI.OCRDialog import OCRDialog

from ownlib.GUI.GridDialog import GridDialog

from ownlib.GUI.MainWindow import MainWindow


def runTest(frame,nb):
	win = ParamPanel(nb)

if __name__ == '__main__':
	app = wx.App()
	MainWindow(None,title="PercentCurrent - IngressMedal")
	app.MainLoop()
