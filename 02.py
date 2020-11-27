# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 13:23:48 2019

@author: DPM
"""

for row in range(0,11):
    for col in range(1,9):
        if (col==1 or col==2 or col==7 or col==8) or ( (row==0 or row==1) and (col!=1 and col!=2 and col!=7 and col!=8)):
            print("*",end=" ")
        elif((row==5 or row==6) and (col==1 and col==2 and col==7 and col==8)):
            print(" ",end=" ")
        else:
            print(end=" ")
    print()        