class file():
    #for counting number of words
    def count_words(self):
        num_words=0
        with open("mus.txt",'r') as f:
            for line in f:
                words=line.split()
                num_words+=len(words)
        print("number of words:",num_words)

#for counting number of lines
    def count_lines(self):
        num_lines=0
        with open("mus.txt",'r') as f:
            for line in f:
                
                num_lines+=1
        print("number of lines:",num_lines)

#count no. of void spaces
    def count_voidspaces(self):
        k=0
        with open("mus.txt",'r') as f:
            for line in f:
                words=line.split()
                for i in words:
                    for letter in i:
                        if(letter.isspace):
                            k=k+1
        
        print("number of void sapces are:",k)


obj=file()
print("1:words\n2:lines\n3:spaces\n4:exit")
ch=int(input("enter your choice"))
if(ch==1):
    obj.count_words()
elif(ch==2):
    obj.count_lines()
elif(ch==3):
    obj.count_voidspaces()    
else:
    exit()       