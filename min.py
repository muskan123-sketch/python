# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 13:10:19 2019

@author: DPM
"""
#max
a=input("enter any string")
min=a[0]
for i in range(len(a)):
    if(min>a[i]):
        min=a[i]
print(min)        
        