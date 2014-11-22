# -*- coding: utf-8 -*-
import wx
import wx.grid
from ownlib.Current import Current
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