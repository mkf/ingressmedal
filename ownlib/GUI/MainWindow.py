# -*- coding: utf-8 -*-
import wx
import wx.grid
from ownlib.Current import Current


ID_MENU_NEWAGENT = wx.NewId()
ID_MENU_SWITCHAGENT = wx.NewId()
ID_MENU_DELENTRY = wx.NewId()
ID_MENU_SHOWHISTFRAG = wx.NewId()
ID_MENU_SHAREHISTFRAG = wx.NewId()
ID_MENU_SHAREENTRY = wx.NewId()
ID_MENU_SHARECHERRYENTRIES = wx.NewId()
ID_MENU_SHAREAGENT = wx.NewId()
ID_MENU_EXPORTBACKUP = wx.NewId()
ID_MENU_IMPORTSHARED = wx.NewId()
ID_MENU_IMPORTBACKUP = wx.NewId()
ID_MENU_NEWDB = wx.NewId()
ID_MENU_OPENDB = wx.NewId()
class MainWindow(wx.Frame):


	def __init__(self,parent,title):
		super(MainWindow,self).__init__(parent,title=title,size=(1200,720))
		menubar = wx.MenuBar()
		filemenu = wx.Menu()
		menu = {}
		menu['NewAgent'] = filemenu.Append(ID_MENU_NEWAGENT,"New Agent","Create a new Agent")
		menu['SwitchAgent'] = filemenu.Append(ID_MENU_SWITCHAGENT,"Switch Agent","Switch between Agents")
		menu['DelEntry'] = filemenu.Append(ID_MENU_DELENTRY,"Delete Entry","Choose an entry to delete")
		menu['ShowHistFrag'] = filemenu.Append(ID_MENU_SHOWHISTFRAG,"Show a fragment of history","Choose starting and ending entries to show everything between them")
		menu['ShareHistFrag'] = filemenu.Append(ID_MENU_SHAREHISTFRAG,"Share a fragment of history","Choose starting and ending entries to share everything between them")
		menu['ShareEntry'] = filemenu.Append(ID_MENU_SHAREENTRY,"Share an entry","Choose an entry to share")
		menu['ShareEntriesCherry'] = filemenu.Append(ID_MENU_SHARECHERRYENTRIES,"Share cherry-picked entries","Choose by cherry-picking the entries you want to share")
		menu['ShareAgent'] = filemenu.Append(ID_MENU_SHAREAGENT,"Share an Agent","Choose the agent to share all the information about")
		menu['ExportEverything'] = filemenu.Append(ID_MENU_EXPORTBACKUP,"Export data&config backup","Export the whole database and configuration files")
		menu['ImportShared'] = filemenu.Append(ID_MENU_IMPORTSHARED,"Import shared file","Choose a file shared to you by someone")
		menu['ImportEverything'] = filemenu.Append(ID_MENU_IMPORTBACKUP,"Import a data&config backup","Choose a data&config backup and import what you want")
		menu['NewDB'] = filemenu.Append(ID_MENU_NEWDB,"Create a new database","Create a new database file in another path and switch to it")
		menu['SwitchDB'] = filemenu.Append(ID_MENU_OPENDB,"Open another database","Switch to another database file")
		menubar.Append(filemenu, '&File')
		self.SetMenuBar(menubar)
		self.InitUI()
		self.Centre()
		self.Show()

	def InitUI(self):
		panel = wx.Panel(self,-1)

		font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
		font.SetPointSize(8)

		vs = wx.BoxSizer(wx.HORIZONTAL)
		#box1_title = wx.StaticBox(panel,-1,"Parameters")
		#box1 = wx.StaticBoxSizer(box1_title,wx.VERTICAL)

		butgrid = wx.FlexGridSizer(cols=3)
		opencreateentrybut = wx.Button(panel,label="Create New Entry")
		opencreateentrybut.Bind(wx.EVT_BUTTON,self.OnCreateEntryChoose)
		butgrid.Add(opencreateentrybut,0,wx.EXPAND)
		vs.Add(butgrid,1,wx.EXPAND,40)

		panel.SetSizer(vs)
		vs.Fit(panel)
		panel.Move((50,50))

		#print a

	def OnCreateEntryChoose(self,e):
		print e