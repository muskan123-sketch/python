# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 18:22:55 2019

@author: DPM
"""

import pandas as pd
import numpy as np
q1=[92,93,95,98]
q2=[96,97,98,85]
q3=[86,87,88,76]
dic={'101':q1,'102':q2,'103':q3}
df=pd.DataFrame(dic,index=[['fy','fy','sy','sy'],['sem-1','sem-2','sem-1','sem-2']],columns=['101','102','103'])
print(df)