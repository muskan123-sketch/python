avail=['b1','b2','b3','b4','b5','b6','b7','b8','b9','b10','b11','b12']
issued=[]    
def enquirey():
    d=input("enter the book")
    for i in avail:
        if(i==d):
            break
    if(i==d):
        print("book availiable:",d)
    else:
        print("not availiable")        
    
def issue():
    e=input("enter the book you want to issue")
    for i in avail:
        if(i==e):
            break
        
    if(i==e):
        print("book issued",e)
        print("you have 30 days to return the book")
        issued.append(i)
        avail.remove(e)
    
    else:
        print("book issued to another student")        
def returnb():
    f=input("enter the book you want to return")
    for i in issued:
        if(i==f):
            break
    if(i==f):
        avail.append(i)
        issued.remove(f)
        print("book returned")
    else:
        print("this book is not issued")
def fine():
    
    h=int(input(" no. of extra days the book was with you"))
    fin=h*2
    y=str(fin)
    print("fine for book is",fin)
    fp=open("library.txt",'a')    
    fp.write("FINE IS:")
    fp.write(y)
    fp.close()


    
    
    
    
    

print(" Welcome to the Library")
while(1):
    
    print("1:enquirey\n2:issue\n3:return\n4:fine\n5:exit\n")
    ch=int(input("enter your choice"))

    if(ch==1):
        enquirey()
    elif(ch==2):
        issue()
    elif(ch==3):
        returnb()
    elif(ch==4):
        fine()
    elif(ch==5):
        break    
fp=open("library.txt",'w')
fp.write("WELCOME TO THE LIBRARY")
fp.write("\n")
fp.write("\n")
fp.write("AVAILIABLE BOOKS ARE")
fp.write("\n")

fp.close()

for i in avail:
    fp=open("library.txt",'a')
    fp.write(i)
    fp.write("\n")
    fp.close()

fp=open("library.txt",'a')    
fp.write("ISSUED BOOKS ARE")
fp.write("\n")
fp.close()

for i in issued:
    fp=open("library.txt",'a')
    fp.write(i)
    fp.write("\n")
    fp.close() 

    

print("availiable books are",avail)
print("issued books are",issued)
    