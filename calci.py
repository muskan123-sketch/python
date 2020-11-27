#design a calculator
#Add,Substract,Multiply,Divide
def Add(a,b):
    c=a+b
    print(a,"+",b,=,c)
def Substract(a,b):
    c=a-b
    print(a,"-",b,=,c)
def Multiply(a,b):
    c=a*b
    print(a,"*",b,=,c)
def Divide(a,b):
    c=a/b
    print(a,"/",b=,c)
while(1):
    print("1.Add\n2.Substract\n3.Multiply\n4.Divide")
    choice=int(input("enter your choice"))
if(choice==1):
    Add(a,b) 
elif(choice==2):
    Substract(a,b)
elif(choice==3):
    Multiply(a,b)           
elif(choice==4):
    Divide(a,b)
else:
    exit(0)
