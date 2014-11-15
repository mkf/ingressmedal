#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import argparse
import wx
from Current import Current

class MainWindow(wx.Frame):
	def __init__(self,parent,title):
		wx.Frame.__init__(self,parent,title=title,size=(200,100))
