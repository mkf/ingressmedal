#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import argparse
import wx
from Current import Current

def TrueOrFalse(ciag):
	if (ciag == "True") or (ciag == "y") or (ciag == "yes"):
		return True
	elif (ciag == "False") or (ciag == "n") or (ciag == "no"):
		return False
	else:
		raise argparse.ArgumentTypeError('It is not True nor False, y nor n, yes nor no. Although it had to.')


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
			raise argparse.ArgumentTypeError('It is not "n" nor a number. Although it had to.')


argh = argparse.ArgumentParser()

from interactive import Interactive


interaktywnosciowo = Interactive()
argumentydodane = []
for keyowo in interaktywnosciowo.GivMeCurQSdict().keys():
	argh.add_argument(
		('-' + keyowo),
		('--' + keyowo),
		type=int,
		help=(interaktywnosciowo.GivMeCurQSdict()[keyowo]))
	argumentydodane.append(keyowo)
for keyowko in interaktywnosciowo.GivMeCurQUSdict().keys():
	argh.add_argument(
		('-' + keyowko),
		('--' + keyowko),
		type=BigNumberORn,
		help=(interaktywnosciowo.GivMeCurQUSdict()[keyowko]))
	argumentydodane.append(keyowo)
argh.add_argument('-i', '--interactively', type=TrueOrFalse, help="Interactively (True/False)")
argh.add_argument('-o', '--overs', type=TrueOrFalse, help="Show overs (True/False)")
parmetry = vars(argh.parse_args())

class MainWindow(wx.Frame):
	def __init__(self,parent,title):
		wx.Frame.__init__(self,parent,title=title,size=(1200,720))
		self.CreateStatusBar()
		filemenu = wx.Menu()
		menuNewAgent = filemenu.Append(wx.ID_NEW,"New Agent","Create a new Agent")
		menuSwitchAgent = filemenu.Append(wx.ID_FILECTRL,"Switch Agent","Switch between Agents")
		menuNewEntry = filemenu.Append(wx.ID_NEW,"New Entry","Create a new stats entry")
		menuDelEntry = filemenu.Append(wx.ID_DELETE,"Delete Entry","Choose an entry to delete")
		menuShowHistFrag = filemenu.Append(wx.ID_JUMP_TO,"Show a fragment of history","Choose starting and ending entries to show everything between them")
		menuShareHistFrag = filemenu.Append(wx.ID_SAVEAS,"Share a fragment of history","Choose starting and ending entries to share everything between them")
		menuShareEntry = filemenu.Append(wx.ID_SAVEAS,"Share an entry","Choose an entry to share")
		menuShareEntriesCherry = filemenu.Append(wx.ID_SAVEAS,"Share chery-picked entries","Choose by cherry-picking the entries you want to share")
		menuShareAgent = filemenu.Append(wx.ID_SAVEAS,"Share an Agent","Choose the agent to share all the information about")
		menuExportEverything = filemenu.Append(wx.ID_SAVEAS,"Export data&config backup","Export the whole database and configuration files")
		menuImportShared = filemenu.Append(wx.ID_OPEN,"Import shared file","Choose a file shared to you by someone")
		menuImportEverything = filemenu.Append(wx.ID_OPEN,"Import a data&config backup","Choose a data&config backup and import what you want")

class ParamPanel(wx.Panel):
	def __init__(self,parent):
		wx.Panel.__init__(self,parent,-1)
		panel = wx.Panel(self,-1)
		vs = wx.BoxSizer(wx.HORIZONTAL)
		box1_title = wx.StaticBox(panel,-1,"Parameters")
		box1 = wx.StaticBoxSizer(box1_title,wx.VERTICAL)
		grid1 = wx.FlexGridSizer(cols=2)
		self.group1_ctrls = []
		te1 = wx.StaticText(panel,-1,"Te")
		te2 = wx.StaticText(panel,-1,"Te")
		te3 = wx.StaticText(panel,-1,"Te")
		text1 = wx.SpinCtrl(panel,-1,"")
		text2 = wx.SpinCtrl(panel,-1,"")
		text3 = wx.SpinCtrl(panel,-1,"")
		self.group1_ctrls.append(te1,text1)
		self.group1_ctrls.append(te1,text2)
		self.group1_ctrls.append(te1,text3)

		for te, text in self.group1_ctrls:
			grid1.Add(te,0,wx.ALIGN_CENTRE|wx.LEFT|wx.RIGHT|wx.TOP,5)
			grid1.Add(text,0,wx.ALIGN_CENTRE|wx.LEFT|wx.RIGHT|wx.TOP,5)

		panel.SetSizer(vs)
		vs.Fit(panel)
		panel.Move((50,50))
		self.panel = panel



def runTest(frame,nb):
	win = ParamPanel(nb)

if __name__ == '__main__':
	app = wx.App()
	MainWindow(None,title="PercentCurrent - IngressMedal")
	app.MainLoop()
