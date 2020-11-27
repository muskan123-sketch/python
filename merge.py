# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 00:10:22 2019

@author: DPM
"""

import pandas as pd
data1={'key':['K0','K1','K2','K3'],
       'key1':['K0','K1','K0','K1'],
       'Name':['jai','quona','ray','deepti'],
       'Age':[27,22,23,24]}
data2={'key':['K0','K1','K2','K3'],
       'key1':['K0','K0','K0','K1'],
       'Address':['nagpur','dhar','dewas','mumbai'],
       'Qualification':['btech','B.A','Bcom','Bhons']}
df=pd.DataFrame(data1)
df1=pd.DataFrame(data2)
print(df,"\n\n",df1)
res=pd.merge(df,df1,how='left',on=['key','key1'])
print(res)
res=pd.merge(df,df1,how='right',on=['key','key1'])
print(res)
res=pd.merge(df,df1,how='outer',on=['key','key1'])
print(res)
