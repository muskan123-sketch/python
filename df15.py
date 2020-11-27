# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 10:14:29 2019

@author: DPM
"""

import pandas as pd
import numpy as np
sub=['pens','pencils','erasers']
l=[96,92,98,96,92,90,91,93,98,89,90,90]
df=pd.DataFrame(np.array(l).reshape(4,3),index=['2001','2002','2003','2004'],columns=['pens','pencils','erasers'])
print(df)
print("***************************************************************************************")

class rank:
    def __init__(self,a):
        self.a=a
    def average_rank(self):
        df['rank_avg',self.a]=df[self.a].rank(axis=0,method='average')
    def maximum_rank(self):
        df['rank_max',self.a]=df[self.a].rank(axis=0,method='max')
    def minimum_rank(self):
        df['rank_min',self.a]=df[self.a].rank(axis=0,method='min')
    def dense_rank(self):
        df['rank_dense',self.a]=df[self.a].rank(axis=0,method='dense')

while(1):
    df.columns
    inp=input("Enter the name of Product")        
    obj=rank(inp)
    n=input("1. average_rank\n2. maximum_rank\n3. minimum_rank\n4. dense_rank")
    if(n==1):
        obj.average_rank()
    elif(n==2):
        obj.maximum_rank()
    elif(n==3):
        obj.minimum_rank()
    elif(n==4):
        obj.dense_rank()
    elif(n==5):
        break
    else:
        print("WRONG CHOICE")

    print(df)