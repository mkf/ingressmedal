# -*- coding: utf-8 -*-
import wx
import wx.grid
from ownlib.Current import Current
class NewEntryDialog(wx.Dialog):
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