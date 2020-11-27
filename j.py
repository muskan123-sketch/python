# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 09:27:03 2019

@author: DPM
"""

print(df.swaplevel(0,1,axis=1))
#project a given student record
a=int(input("enter the rollno: "))
p=df.iloc[a,:]
print(p)
                  