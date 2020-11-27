# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 14:06:56 2019

@author: DPM
"""

from matplotlib import pyplot as pt
import pandas as pd
df=pd.read_excel("hack.xlsx")
df.set_index(['year','hacktype'],inplace=True)
print(df)
g=df.groupby(["year"])["city1"].sum()
print(g)
v=df.groupby(["year"])["city1"].mean()
print(v)
f=df.groupby(["year","hacktype"])["city1"].sum()
print(f)

#f.plot.bar(color='green')
#print(f)
#g.plot.pie()
#print(g)
#g.plot(color='green')
#print(g)
#g.plot.bar(color='green')
#print(g)
import numpy as np
s=[2,10,4,3,11,4,4,12,9,5,13,8,6,15,12,7,17,13,8,20,16,9,21,11,10,23,8]
df=pd.DataFrame(np.array(s).reshape(9,3),index=[['year1','year1','year1','year2','year2','year2','year3','year3','year3'],['hacking','onlinefraud','dos','hacking','onlinefraud','dos','hacking','onlinefraud','dos']],columns=['city1','city2','city3'])
print(df)
print("***********************visualisation of above dataframe**************")
h=df.loc[('year1'),:]
print(h)
h.plot.bar(color=['red','pink','cyan'])
pt.show()
l=df.loc[('year1'),:'city1']
print(l)
q=['hacking','onlinefraud','dos']
pt.scatter(q,l)
pt.show()
f=df.loc[('year1','hacking'),:].max()
print(f)


#pt.plo9t(months,h)
#pt.xlabel('months')
#pt.ylabel('ONEBHK')
3#pt.show()