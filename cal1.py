print("1 integral calculator 2 float calculator")
ty=int(input(" enter the type of calculator"))

if(ty==1):                                              # INTEGRAL CALCULATOR
    
    print("INTEGRAL CALCULATOR")
    a=int(input(" Enter first number"))
    b=int(input(" Enter second number"))
else:                                                   # FLOAT CALCULATOR
    print("FLOAT CALCULATOR")
    a=float(input("Enter first number"))
    b=float(input("Enter second number"))    


def addition():
    c=a+b
    return c

def subtraction():
    s=a-b
    return s

def multiplication():
    m=a*b
    return m

def division():
    d=a/b
    return d

print("1 addition\n 2 subtraction \n3 multiplicaton \n4 subtraction")
choice=int(input("enter the choice"))


if(choice==1):
    add=addition()
    print("addition=",add)
elif(choice==2):
    sub=subtraction()
    print("subtraction",sub)
elif(choice==3):
    mul=multiplication()
    print("multiplicaion=",mul)
elif(choice==4):
    div=division()
    print("division=",div)
else:
    print(" wrong choice")




    