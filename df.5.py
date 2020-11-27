# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 19:45:16 2019

@author: DPM
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as pt
roll_no=[1,2,3,4]
sub=['s1','s2','s3']
sum=0
l=[96,97,98,99,92,90,91,87,88,89,90,98]
df=pd.DataFrame(np.array(l).reshape(4,3),index=['r1','r2','r3','r4'],columns=['s1','s2','s3'])
print(df)
print("-------------------------")
#visualise performance in each subject
b=int(input("enter the subject[0-s1,1-s2,2-s3]: "))
d=df.iloc[:,b]
pt.bar(roll_no,d)
pt.xlabel('roll_no')
pt.ylabel('subjects')
pt.title('info')
pt.show()
#average attendance of all students in each subject
b=int(input("enter the subject[0-s1,1-s2,2-s3]: "))
for i in range(0,4):
    v=df.iloc(i,b)
    sum=sum+v
average=sum/4
print(average) 
print("-------------------------")
#display top 2 students in each subject
b=int(input("enter the subject[0-s1,1-s2,2-s3]: "))
j=df.iloc[:,b]
h=df.nlargest(2,j)
print("the two toppers of the subject is",roll_no)



  




    
