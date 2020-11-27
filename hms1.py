# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 16:23:22 2019

@author: DPM
"""

print("*************WRITE A PROGRAM TO IMPLEMENT Hospital Management System using text file and perform following operations****************************************")
pat_info=[]
uni=['ram','shyam','sita','gita','hari','joey','dromey','bhoem','lisa']
D1=['ram','sita','gita']                     #eye department
D2=['joey','dromey','bhoem']                     #dentist department
D3=['lisa','hari','shyam']                     #heart department
dis1=['astigatism','colourblindness','corneadamage']
dis2=['cavities','oralcancer','sensitiveteeth']
dis3=['heartattack','highbp','arrhythmia']
def add():
    g=input("enter your name:")
    uni.append(g)
    f=input("enter the department:")
    if(f=='D1'):
        D1.append(g)
    elif(f=='D2'):
        D2.append(g)
    elif(f=='D3'):
        D2.append(g)    
    print("enter the type of disease\n 1.eye\n 2.dental\n 3.heart")
    v=int(input("enter your choice"))
    if(v==1):
        h=input("enter the disease:")
        dis1.append(h)
    elif(v==2):
        h=input("enter the disease:")
        dis2.append(h)
    elif(v==3):
        h=input("enter the disease:")
        dis3.append(h)    
  

    
def search():#to search a patient
    name=input("enter patient name:")
    for i in uni:
        if(i==name):
            break
    if(i==name):
        print("patient is been admitted to hospital:",name)
    else:
        print("not available")
        
    
def srchdeptwise():#to search patient department wise  
    dep=input("enter your department from D1,D2,D3:")
    if(dep=='D1'):
        name=input("enter patient name:")
        for i in D1:
            if(i==name):
                break
        if(i==name):
            print("patient is available in department:",dep)
        else:
            print("not available")
    if(dep=='D2'):
        name=input("enter patient name:")
        for i in D2:
            if(i==name):
                break
        if(i==name):
            print("patient is available in department:",dep)
        else:
            print("not available")
    if(dep=='D3'):
        name=input("enter patient name:")
        for i in D3:
            if(i==name):
                break
        if(i==name):
            print("patient is available in department:",dep)
        else:
            print("not available")    
def displaydis():
    print("enter the category of disease you want to display \npress1 for displaying eye realated disease\n press2 for displaying dental disease\n 3for displaying heart realated disease")
    l=int(input("enter your choice:")) 
    if(l==1):
        print(dis1)
    elif(l==2):
        print(dis2)
    elif(l==3):
        print(dis3) 
        
#def dispdiswise():#to search a patient disease wise  
    
while(1):
    print('press1 to add\n press2 to search patient\n press3 to search patient depatment wise\n press4 to display patient disease wise\n press5 exit')
    choice=int(input("enter your choice:"))
    if(choice==1):
        add()
    elif(choice==2):
        search()
    elif(choice==3):
        srchdeptwise()
    elif(choice==4):
        displaydis()
    elif(choice==5):
        break
print("patients admitted are",uni) 
fp=open("hospital.txt",'w')
fp.write("WELCOME TO HOSPITAL MANAGEMENT")
fp.write("\n")
fp.write("\n")
fp.write("patients admitted are")
fp.write("\n")
fp.close()
for i in uni:
    fp=open("hospital.txt",'a')
    fp.write(i)
    fp.write("\n")
    fp.close()    
fp=open("hospital.txt",'a') 
fp.write("patients of department 1 are:")
fp.write("\n")
fp.close()
for i in D1:
    fp=open("hospital.txt",'a')
    fp.write(i)
    fp.write("\n")
    fp.close()
fp=open("hospital.txt",'a') 
fp.write("patients of department 2 are:")
fp.write("\n")
fp.close()
for i in D2:
    fp=open("hospital.txt",'a')
    fp.write(i)
    fp.write("\n")
    fp.close() 
fp=open("hospital.txt",'a') 
fp.write("patients of department 3 are:")
fp.write("\n")
fp.close()
for i in D3:
    fp=open("hospital.txt",'a')
    fp.write(i)
    fp.write("\n")
    fp.close()
fp=open("hospital.txt",'a') 
fp.write("various disease of eye are:")
fp.write("\n")
fp.close()
for i in dis1:
    fp=open("hospital.txt",'a')
    fp.write(i)
    fp.write("\n")
    fp.close()
fp=open("hospital.txt",'a') 
fp.write("various disease of dental are:")
fp.write("\n")
fp.close()
for i in dis2:
    fp=open("hospital.txt",'a')
    fp.write(i)
    fp.write("\n")
    fp.close()
fp=open("hospital.txt",'a') 
fp.write("various disease of heart are:")
fp.write("\n")
fp.close()
for i in dis3:
    fp=open("hospital.txt",'a')
    fp.write(i)
    fp.write("\n")
    fp.close()       
    
       
       

   
    
    
        
        
        