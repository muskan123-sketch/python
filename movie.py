# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 11:02:56 2019

@author: DPM
"""

import pandas as pd
import numpy as np
s=[56,57,58,59,60,61,62,63,64,65,66,67,69,90,89,97,95,94,93,73,56,57,58,59,60,61,62,63,64,65]
df=pd.DataFrame(np.array(s).reshape(5,6),index=['horror','action','romantic','thriller','comedy'],columns=[['2018','2018','2018','2019','2019','2019'],['pune','banglore','delhi','pune','banglore','delhi']])
print(df)