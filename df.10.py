# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 13:00:21 2019

@author: DPM
"""

import pandas as pd
import numpy as np
total=0
roll_no=[1,2,3,4]
sub=['maths','ds','phy']
l=[96,92,98,96,92,90,91,93,98,89,90,90]
df=pd.DataFrame(np.array(l).reshape(4,3),index=['ex1','ex2','ex3','ex4'],columns=['maths','ds','phy'])
print(df)
print("-------------------------")
s=df.sum(axis=1)
print(s)
df['total']=s
print("***************************************************************************************")
df['R-m']=df['maths'].rank()
#df['R-m_mx']=df['maths'].rank(method='max')
df['R-m_mn']=df['maths'].rank(method='min')

df['R-d']=df['ds'].rank()
#df['R-d_mx']=df['ds'].rank(method='max')
df['R-d_mn']=df['ds'].rank(method='min')


df['R-p']=df['phy'].rank()
#df['R-p_mx']=df['phy'].rank(method='max')
df['R-p_mn']=df['phy'].rank(method='min')


df['R-t']=df['total'].rank()
print(df)
print("********************************************************************************************")
