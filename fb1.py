# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 22:23:45 2019

@author: DPM
"""
from matplotlib import pyplot as pt
import pandas as pd
df=pd.read_excel("fb5.xlsx",header=[0,1],index_col=0)
print(df)
print("******city wise rate of usage******")
print(" fb ")
print("(city1,city2,city3)")
p=['city1','city2','city3']

df1=df.groupby([('fb','city1'),('fb','city2'),('fb','city3')])

for i,i_df in df1:
    
    print(i)
df1.plot.bar()
pt.show() 
l=df.loc[:,('fb','city1')]   
print(l)
l.plot()
pt.show()
l.plot.bar()
pt.show()
l.plot.pie()
pt.show()

pt.scatter(p,l)
pt.show()


#df.set_index(['time'],inplace=True)
#s=df.sum(axis=0)
#print(s)
#df['total']=s
#print(s)
#print("--------------------------------------")
#print(df.swaplevel(0,1,axis=1))
#print("--------------------------------------")
#print(df.stack())


                  

#g=df.groupby(['time'])['fb'].sum()
#print(g)
#g.plot.bar(color="blue")
#pt.show()