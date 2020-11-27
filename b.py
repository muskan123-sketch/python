# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 18:12:17 2019

@author: DPM
"""
import pandas as pd
s3 = pd.Series([0, 1, 2, 3], name='foo')
s4 = pd.Series([0, 1, 2, 3])
s5 = pd.Series([0, 1, 4, 5])
s=pd.concat([s3, s4, s5], axis=0)
print(s)
