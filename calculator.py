#design a calculator
#add,substract,multiply,divide
def Add(a,b):   #to add two numbers
    c=a+b
    print(a,"+",b,"=",c) 
def Substract(a,b): #to substract two numbers
    c=a-b
    print(a,"-",b,"=",c) 
def Multiply(a,b):           #to multiply numbers
    c=a*b
    print(a,"*",b,"=",c)
def Divison(a,b):#to divide numbers 
    c=a/b
    print(a,"/",b,"=",c)
while True :
    print("1.Add\n2.Substract\n3.Multiply\n4.Divide\n5.exit")
    choice=int(input("enter your choice : "))
    a = int(input("enter one number :"))
    b= int(input("enter a number : "))
    if(choice==1):
           Add(a,b) 
    elif(choice==2):
           Substract(a,b)
    elif(choice==3):
           Multiply(a,b)
    elif(choice==4):
           Divison(a,b)
    else:
           exit(0)               
    