print("**********************************************************")
print ("                    WELCOME TO ANAND MALL")
print("**********************************************************")
import numpy as np
import pandas as pd
class Shopping:
    def __init__(self,a):
        self.a=a
             
    def price(self):
        pr=self.a
        if(pr==1):
            cost=300
            cart.append(item[0])
            return cost
        
        elif(pr==2):
            cost=20
            cart.append(item[1])
            return cost
        elif(pr==3):
           cost=45
           cart.append(item[2])
           return cost
        elif(pr==4):
           cost=100
           cart.append(item[3])
           return cost
        elif(pr==5):
           cost=250
           cart.append(item[4])
           return cost
        elif(pr==6):
           cost=300
           cart.append(item[5])
           return cost
        elif(pr==7):
           cost=15
           cart.append(item[6])
           return cost
        elif(pr==8):
           cost=75
           cart.append(item[7])
           return cost
        elif(pr==9):
           cost=500
           cart.append(item[8])
           return cost
        elif(pr==10):
           cost=160
           cart.append(item[9])
           return cost
cart=[]            
prod_code=np.arange(1,11)
item=["jam","bread","biscuit","hand wash","shampoo","perfume","pen","chocolate","wallnut","raisens"]
price=[300,20,45,100,250,300,15,75,500,160]
dict={'prod_code':prod_code,'item':item,'price':price}
df=pd.DataFrame(dict)
print (df)

n=int(input("enter the no. of item you want to purchase :"))
amt=0

for i in range(0,n):
    a=int(input("enter product code of the item you want to purchase"))
    o=Shopping(a)
    cost=o.price()
    #print(cost)
    amt=amt+cost
print ("total amount to be paid is :")
print(amt)


price_range=["P<500","500<=P<800","800<=P<1200","1200<=P<1500","P>=1500"]
COUPOUN=["   ","10OFF","15OFF","20OFF","30OFF"]
OFFER=["NO DISCOUNT","10% OF ON TOTAL","15% OF ON TOTAL","20% OF ON TOTAL","30% OF ON TOTAL"]
dict1={'PRICE_RANGE':price_range,'COUPOUN':COUPOUN,'OFFER':OFFER}
df=pd.DataFrame(dict1)
print(df)


code=input("enter the coupoun code")
if(code=="10OFF"):
    if(amt>=500 and amt<800):
        print("valid code")
        print("congratulations discount is applied")
        final_amt=(amt-((10/100)*amt))
        print("final amount after discount is :")
        print("TOTAL AMOUNT:",final_amt)
    else:
        print("invalid code")
        

elif(code=="15OFF"):
    if(amt>800 and amt<1200):
        print("valid code")
        print("congratulations discount is applied")
        final_amt=(amt-((15/100)*amt))
        print("final amount after discount is :")
        print("TOTAL AMOUNT:",final_amt)
    else:
        print("invalid code")


elif(code=="20OFF"):
    if(amt>1200 and amt<1500):
        print("valid code")
        print("congratulations discount is applied")
        final_amt=(amt-((20/100)*amt))
        print("final amount after discount is :")
        print("TOTAL AMOUNT:",final_amt)
    else:
        print("invalid code")

elif(code=="30OFF"):
    if(amt>=1500):
        print("valid code")
        print("congratulations discount is applied")
        final_amt=(amt-((30/100)*amt))
        print("final amount after discount is :")
        print("TOTAL AMOUNT:",final_amt)
    else:
        print("invalid code")
print("your cart is:",cart)        
print("         THANK YOU FOR SHOPPING WITH US")

