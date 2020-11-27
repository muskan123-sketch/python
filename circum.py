# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 10:27:44 2019

@author: DPM
"""

class circumference :
    def __init__(self,r):
        self.r=r
    def cal(self):
        cir= 2*3.14*(self.r)
        print("circumference is",cir)
r=int(input("enter the value of r"))
obj=circumference(r)
obj.cal()    
        
        