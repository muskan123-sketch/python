# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 09:55:45 2019

@author: DPM
"""

import pandas as pd
import numpy as np
l=[1,2,3,4,5,6,7,8,9]
df1=pd.DataFrame(np.array(l).reshape(3,3),index=['0','1','2'],columns=['A','B','C'])
print(df1)
K=[3,6,9,18,19,20]
df2=pd.DataFrame(np.array(K).reshape(3,2),index=['3','4','5'],columns=['C','E'])
print(df2)
df3=pd.merge(df1,df2,on='C',how='outer')
df4=pd.merge(df1,df2,on='C')
df5=pd.concat([df1,df2])
print(df5)
print(df3)
print(df4)
print("-------------------------")