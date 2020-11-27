# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 12:56:44 2019

@author: DPM
"""

import pandas as pd
MH=[19,20,21]
UP=[22,23,24]
DH=[25,26,27]
index=[2001,2002,2003]
POP={'MH':MH,'UP':UP,'DH':DH}
df=pd.DataFrame(POP,index=[index])
print(df)
