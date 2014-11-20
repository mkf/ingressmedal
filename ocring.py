#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ownlib.OcrRead import OcrRead
import argparse
argh = argparse.ArgumentParser()
argh.add_argument('-f','--fromimage',type=str,help="Specify image file",required=True)
argh.add_argument('-c','--cache',type=str,help="Specify .pbm image cache file",required=True)
parmetry = vars(argh.parse_args())
o = OcrRead()
print o.ocrad_get(parmetry['fromimage'],parmetry['cache'])