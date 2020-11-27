# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 12:03:25 2019

@author: DPM
"""

#to design an employee management system
mgr=[]
prohead=[]
deve=[]
count=0
bcount=0
ccount=0
class emp_info:
    def __init__(self,name,desig):
        self.name=name
        self.desig=desig
    def insert():
        empl.append(mgr)
        empl.append(prohead)
        empl.append(deve)
        if(desig==manager):
            count=count+1
            a="18"+"01"+str(count)
            mgr.append(a)
            mgr.append(name)
            mgr.append(desig)
        elif(desig==projecthead):
            bcount=bcount+1
            b="18"+"02"+str(bcount)
            prohead.append(b)
            prohead.append(name)
            prohead.append(desig)
        elif(desig==developer):
            ccount=ccount+1
            c="18"+"03"+str(ccount)
            deve.append(c) 
            deve.append(name)
            deve.append(desig)
    def display():
        if(len(emp_info)==0):
            print("list is empty")
        else:
            for i in emp_info:
                print(i)
while(1):
    print('press1 to insert record\npress2 to display records\npress3 to exit')
    ch=input("enter your choice")
    if(ch==1):
        name=input("enter employee name:")
        desig=inut("enter your desig:")
        obj=emp_info(name,desig)
        obj.insert()
    elif(ch==2):
        obj=emp_info(name,desig)
        obj.display()
    else:
        exit()

                         






                

