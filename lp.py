# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 22:28:46 2019

@author: DPM
"""
#import numpy as np
import pandas as pd
name_1=["Viplav" ,"Viplav","Aakash","Aakash","Vikash","Vikash","Ashutosh","Ashutosh","Kamal","Kamal"]
sem=["L","P","L","P","L","P","L","P","L","P"]

subject={'sub1':[23,92,67,52,45,58,34,34,24,23],'sub2':[44,69,68,66,58,87,85,96,96,45],'sub3':[98,39,66,67,49,96,38,58,78,24]}
df5=pd.DataFrame(data=subject,index=[name_1,sem],columns=['sub1','sub2','sub3'])
print(df5)
sa=df5.mean(axis=1)
df5['Average']=sa
print(df5)
f=df5.loc[("Viplav"),:]
print(f)

#print("--------------------------------------")
#print(df.swaplevel(1,0,axis=0))

