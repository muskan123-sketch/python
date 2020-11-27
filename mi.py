# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 09:45:50 2019

@author: DPM
"""

import pandas as pd
import numpy as np
df=pd.DataFrame(np.arange(12).reshape(4,3),index=[['fy','fy','sy','sy'],['sem-1','sem-2','sem-1','sem-2']]
,columns=['101','102','103'])
print(df)
print("--------------------------------------")
print(df.swaplevel(0,1,axis=0))
print("--------------------------------------")
print(df.unstack())



