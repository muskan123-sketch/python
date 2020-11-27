# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 12:29:48 2019

@author: DPM
"""

import pandas as pd
import numpy as np
sub=['pens','pencils','erasers']
l=[96,92,98,96,92,90,91,93,98,89,90,90]
df=pd.DataFrame(np.array(l).reshape(4,3),index=['2001','2002','2003','2004'],columns=['pens','pencils','erasers'])
print(df)
print("***************************************************************************************")
df['R-p']=df['pens'].rank()
#df['R-p_mx']=df['pens'].rank(method='max')
#df['R-p_mn']=df['pens'].rank(method='min')
df['R-p_de']=df['pens'].rank(method='dense')

df['R-n']=df['pencils'].rank()
#df['R-n_mx']=df['pencils'].rank(method='max')
#df['R-n_mn']=df['pencils'].rank(method='min')
df['R-n_de']=df['pencils'].rank(method='dense')

df['R-e']=df['erasers'].rank()
#df['R-e_mx']=df['erasers'].rank(method='max')
#df['R-e_mn']=df['erasers'].rank(method='min')
df['R-e_de']=df['erasers'].rank(method='dense')
f=df.sort_index(axis=1)
print(f)
d= df.sort_values(by='erasers')
print(d)

print(df)
print("********************************************************************************************")