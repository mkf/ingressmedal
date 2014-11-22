# -*- coding: utf-8 -*-
import wx
import wx.grid
from ownlib.Current import Current
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