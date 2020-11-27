# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 20:09:59 2019

@author: DPM
"""
#from matplotlib import pyplot as pt
import pandas as pd
f=pd.read_excel("car3.xlsx")
print(f)
#f.set_index(['category','type'],inplace=True)
#print(f)
g=f.groupby(["type"])[("q1","q2","q3","q4")].sum()
print(g)
l=f.groupby(["category"])[("q1","q2","q3","q4")].mean()
#print(l)
#l.plot.bar()
#g.plot.bar()
#g.plot()
e=f.groupby(["type"])["q1"].sum()
print(e)
e.plot.pie(autopct='%1.1f%%', shadow=True, startangle=90)
#maxvalue=f.max()
#print(maxvalue)
#maxvalue=g.max()
#print(maxvalue)
#s=f.sum(axis=1)
#print(s)
#f['total']=s
#print(f)
#d=f[['total']].max()
#print(d)
#k=f.groupby(["type"])["total"].sum()
#print(k)
#k.plot.pie()
#l=f.groupby(["type"])["q1"].mean()
#print(l)
#l.plot.bar()


#print(g)
#g.plot.bar(color="blue")
#pt.show()
#g.plot.bar(color="blue")
#g=df.groupby(["year"])["temperature"].mean()
#print(g)