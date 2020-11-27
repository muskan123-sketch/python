# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 18:41:11 2019

@author: DPM
"""
import matplotlib.pyplot as pt
import pandas as pd
import numpy as np
s=[56,57,58,59,60,61,62,63,64,65,66,67,69,90,89,97,95,94,93,73,56,57,58,59,60,61,62,63,64,65,66,67]
df=pd.DataFrame(np.array(s).reshape(4,8),index=[['g1','g1','g2','g2'],['r1','r2','r3','r4']],columns=[['s1','s1','s1','s2','s2','s3','s3','s3'],['L','P','T','L','P','L','P','T']])

print(df)
f=df.loc[("g1","r1"),:"s1"]
print(f)
g=['lecture','practical','tutorial']
pt.plot(g,f,label='s1')
pt.title("attendance of lecture,practical,tutorial in subject s1")
pt.show()
f=df.loc[("g1","r1"),:"s1"]
print(f)
g=['lecture','practical','tutorial']
pt.bar(g,f,label='s1')
pt.title("attendance of lecture,practical,tutorial in subject s1")
pt.show()
print("--------------------------------------")
#print(df.swaplevel(0,1,axis=1))
#print("--------------------------------------")
#print(df.stack())


                  
