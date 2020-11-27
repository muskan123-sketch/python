# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 13:37:19 2019

@author: DPM
"""

#max
a=input("enter any string: ")
max=a[0]
for i in range(len(a)):
    if(max<a[i]):
        max=a[i]
print(max)        
        