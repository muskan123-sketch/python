# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 07:57:56 2019

@author: DPM
"""

for row in range(7):
    for col in range(5):
        if (col==0) or ((row==0 or row==6) and (col>0)):
            print("*",end=" ")
        else:
            print(end=" ")
    print()        