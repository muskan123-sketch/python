# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 17:00:17 2019

@author: DPM
"""
import numpy as np
import pandas as pd
df = pd.read_excel('Book11.xlsx',header=[0,1],index_col=0)
print(df)
df1=df.groupby([('term1','fc')])
for i,i_df in df1:
    print(i)
print(df['term1','fc'].agg([np.mean,np.sum,min,max,np.std]))  
print(df.swaplevel(0,1,axis=1))
#print("--------------------------------------")
print(df.stack()) 