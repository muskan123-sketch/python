# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 19:03:40 2019

@author: DPM
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as pt
l=[96,97,98,99,92,90,91,87,88,89,90,98]
df=pd.DataFrame(np.array(l).reshape(4,3),index=['r1','r2','r3','r4'],columns=['s1','s2','s3'])
print(df)
print("-------------------------")
#project a given student record
a=int(input("enter the rollno of student [0-r1,1-r2,2-r3,3-r4]: "))
p=df.iloc[a,:]
print(p)
                  
print("-------------------------")
a=int(input("enter the rollno: "))
b=int(input("enter the subject: "))
p=df.iloc[a,b]
print(p)
#visualise performance in each subject
b=int(input("enter the subject[0-s1,1-s2,2-s3]: "))
d=df.iloc[:,b]
pt.bar(rollno,d)
pt.xlabel('rollno')
pt.ylabel('subjects')
pt.title('info')
pt.show()
