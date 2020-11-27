# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 15:39:49 2019

@author: DPM
"""
from matplotlib import pyplot as pt
import pandas as pd
#importing data from excel
df = pd.read_excel('Book11.xlsx',header=[0,1],index_col=0)
print(df)
