# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 14:58:50 2019

@author: DPM
"""

print("*************welcome to bank mangement system****************")
temp=[]
class bank():
    def open_account(self):
    
        name=input("enter your name:")
        dob=input("\nenter your date of birth in dd/mm/yy\:")
        gen=input("\nenter your gender:\n")
        adh=int(input("\nenter your aadhar card number:"))
        pan=int(input("\nenter your pan card number:"))
        add=input("\nenter your addresss:")
        iden="17001700"+str(adh%100)
        temp.append(name)
        temp.append(dob)
        temp.append(gen)
        temp.append(adh)
        temp.append(pan)
        temp.append(add)
        temp.append(iden)

        print(temp)
    def search(self):
        if(len(temp)==0):
            print("customer list is empty")
        else:
            name=input("enter the name of the customer you want to search:")
            for i in temp:
                if(i==name):
                    
                    break
            if(i==name):
                print("our bank has customer with name\n",i)
            else:
                print(" customer not found")
                    
                
    def scheme(self,price):
        print("press1-two year scheme\n press2-five year scheme\n press3-ten year scheme\n press4-fifeteen year scheme")
        ch=int(input("enter your choice:"))
        if(ch==1):
            rate=5
            return( price*rate*2)/100
        elif(ch==2):
            rate=7
            return( price*rate*5)/100
        elif(ch==3):
            rate=9
            return( price*rate*10)/100  
        elif(ch==4):
            rate=12
            return( price*rate*15)/100    
   
obj=bank()
while True:
    print("press1-open new account\n press2-search for a customer\n press3-check term deposit scheme\n press4-exit")
    choice=int(input("enter your choice:")) 
    if(choice==1):
            
        obj.open_account()
    if(choice==2):
            
        obj.search()    
    if(choice==3):
            
        price=int(input("enter deposit amount:"))
        v=obj.scheme(price)
        print(v)
        temp.append(v)
    if(choice==4):
        print("*******THANKYOU********")
        break
fp=open("bank.txt",'w') 
fp.write("welcome to bank mangement system") 
fp.write("\n") 
fp.write("\n")
fp.write("available customer are")
fp.write("\n")
fp.close() 
for i in temp:
    fp=open("bank.txt",'a')
    fp.write(str(i))
    fp.write("\n")
    fp.close()

        
