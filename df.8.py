# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 12:26:26 2019

@author: DPM
"""

import pandas as pd
import numpy as np
total=0
roll_no=[1,2,3,4]
sub=['maths','ds','phy']
l=[96,97,98,99,92,90,91,87,88,89,90,98]
df=pd.DataFrame(np.array(l).reshape(4,3),index=['ex1','ex2','ex3','ex4'],columns=['maths','ds','phy'])
print(df)
print("-------------------------")
s=df.sum(axis=1)
print(s)
df['total']=s
print(df)
df['R-m']=df['maths'].rank()
df['R-d']=df['ds'].rank()
df['R-p']=df['phy'].rank()
df['R-t']=df['total'].rank()
print(df)