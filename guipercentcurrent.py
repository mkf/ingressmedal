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

ID_OPENNEWWNETRYDIALOG = wx.NewId()
ID_OPENOCRDIALOG = wx.NewId()  #OCR dialog will contain image preview and text fields for each medal colour for manual color recognition, and when it will become automatic, it will show them


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

class NewEntryDialog(wx.Dialog):
	def __init__(self,*args,**kw):
		super(NewEntryDialog,self).__init__(*args,**kw)
		self.InitUI()
		self.SetSize((960,960))
		self.SetTitle("New Entry")

	def InitUI(self):
		def InitUI(self):
		panel = wx.Panel(self,-1)

		font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
		font.SetPointSize(8)

		vs = wx.BoxSizer(wx.HORIZONTAL)
		#box1_title = wx.StaticBox(panel,-1,"Parameters")
		#box1 = wx.StaticBoxSizer(box1_title,wx.VERTICAL)
		grid1 = wx.FlexGridSizer(cols=2)
		self.group1_ctrls = []
		# te1 = wx.StaticText(panel,-1,"Te")
		# te1.SetFont(font)
		# te2 = wx.StaticText(panel,-1,"Te")
		# te2.SetFont(font)
		# te3 = wx.StaticText(panel,-1,"Te")
		# te3.SetFont(font)
		# text1 = wx.SpinCtrl(panel,-1,"")
		# text2 = wx.SpinCtrl(panel,-1,"")
		# text3 = wx.SpinCtrl(panel,-1,"")
		# self.group1_ctrls.append((te1,text1))
		# self.group1_ctrls.append((te2,text2))
		# self.group1_ctrls.append((te3,text3))

		from ownlib.gameinfo import gameinfo

		gi = gameinfo()
		gitrmert = []
		gitrmert.extend(gi.listcurrentquestionS)
		gitrmert.extend(gi.listcurrentquestionUS)
		gitrmer = tuple(gitrmert)
		ted = {}
		curQdict = {}
		curQdict.update(gi.currentquestionSdict)
		curQdict.update(gi.currentquestionUSdict)
		from re import sub
		for gitr in gitrmer:
			ted[gitr] = (wx.StaticText(panel,-1,sub(r', ','\n',curQdict[gitr])),wx.SpinCtrl(panel,-1,""))
			ted[gitr][0].SetFont(font)
			self.group1_ctrls.append(ted[gitr])


		for tuptetex in self.group1_ctrls:
			te = tuptetex[0]
			text = tuptetex[1]
			grid1.Add(te,0,wx.ALIGN_LEFT|wx.LEFT|wx.RIGHT|wx.TOP)
			grid1.Add(text,0,wx.ALIGN_CENTRE|wx.LEFT|wx.RIGHT|wx.TOP)

		#midPan = wx.Panel(panel)
		vs.Add(grid1,1,wx.EXPAND,5)

		panel.SetSizer(vs)
		vs.Fit(panel)
		panel.Move((50,50))

		#print a

class OCRDialog(wx.Dialog):
	def __init__(self,*args,**kw):
		super(NewEntryDialog,self).__init__(*args,**kw)
		self.InitUI()
		self.SetSize((960,960))
		self.SetTitle("New Entry")
	def InitUI(self):
		panel = wx.Panel(self,-1)

		font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
		font.SetPointSize(8)

		vs = wx.BoxSizer(wx.HORIZONTAL)
		#box1_title = wx.StaticBox(panel,-1,"Parameters")
		#box1 = wx.StaticBoxSizer(box1_title,wx.VERTICAL)
		butgrid = wx.FlexGridSizer(cols=3)
		vs.Add(butgrid,1,wx.EXPAND,40)
		panel.SetSizer(vs)
		vs.Fit(panel)
		panel.Move((50,50))

class GridDialog(wx.Dialog):
	def __init__(self,*args,**kw):
		super(NewEntryDialog,self).__init__(*args,**kw)
		self.InitUI()
		self.SetSize((960,960))
		self.SetTitle("New Entry")
	def InitUI(self):
		panel = wx.Panel(self,-1)

		font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
		font.SetPointSize(8)

		vs = wx.BoxSizer(wx.HORIZONTAL)
		#box1_title = wx.StaticBox(panel,-1,"Parameters")
		#box1 = wx.StaticBoxSizer(box1_title,wx.VERTICAL)

		exampel = {'sth':[float(2.86),float(2.56),float(5.23)],'asdf':[float(567.3),float(43.5),float(78.4)]}

		mleng = max([len([test for test in exampel[i]]) for i in exampel.keys()])+1


		whathastobe = []
		# ---------------------------\/---there will be a key=head here in sorted() also
		for i in sorted(exampel.keys()):
			whathastobe.append(i)

		grid2 = wx.grid.Grid(self,-1)
		grid2.CreateGrid(len(whathastobe),mleng)
		for i in whathastobe:
			grid2.SetCellValue(whathastobe.index(i),0,str(i))
			grid2.SetReadOnly(whathastobe.index(i),0)
			for j in exampel[i]:
				grid2.SetCellValue(whathastobe.index(i),exampel[i].index(j)+1,str(j))
				grid2.SetReadOnly(whathastobe.index(i),exampel[i].index(j)+1)
		for k in range(1,mleng): grid2.SetColFormatFloat(k,6,3)


		vs.Add(grid2,1,wx.EXPAND|wx.ALIGN_RIGHT,40)

		panel.SetSizer(vs)
		vs.Fit(panel)
		panel.Move((50,50))

		#print a

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
		vs.Add(butgrid,1,wx.EXPAND,40)

		panel.SetSizer(vs)
		vs.Fit(panel)
		panel.Move((50,50))

		#print a

	def OnOCRChoose(self,e):
		pass





def runTest(frame,nb):
	win = ParamPanel(nb)

if __name__ == '__main__':
	app = wx.App()
	MainWindow(None,title="PercentCurrent - IngressMedal")
	app.MainLoop()
