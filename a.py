# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 07:52:18 2019

@author: DPM
"""

for row in range(7):
    for col in range(1,6):
        if ((col==1 or col==5) and row!=0) or ((row==0 or row==3) and (col>1 and col<5)):
            print("*",end=" ")
        else:
            print(end=" ")
    print()        