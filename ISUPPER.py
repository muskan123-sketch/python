# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 00:01:13 2019

@author: DPM
"""

l=[1,2,3,4,5,6,7,8,9,10]
leven=[]
lodd=[]
for i in l:
    if(i%2==0):
        (leven.append(i))
    else:
        (lodd.append(i))
print(leven)
print(lodd)        