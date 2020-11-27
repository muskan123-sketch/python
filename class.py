global count
count = 0
roll_no = 0
# declaring the lists
Std_records = []
batch_a=[]
batch_b=[]
batch_c=[]

class std_rec:

    def __init__(self,name,Prn,gender):
        self.name=name
        self.Prn=Prn
        self.gender=gender

    def insert(self):
    # function to insert data into the list    
        global count
        temp_list = list()
        roll_no = self.Prn % 100
        temp_list.append(roll_no)
        temp_list.append(self.Prn)     
        temp_list.append(self.name)
        temp_list.append(self.gender)
        Std_records.append(temp_list)
        count = count + 1
        return 0

    def display(self):
    # displaying the data in list    
        if(len(Std_records)==0):
            print('Records Are Empty')
        else:
            Std_records.sort()
            for k in Std_records:
                print(k)                
    
    def batch(self):
    # divides the students into respective batches
        Std_records.sort()
        global batch_a
        batch_a=[]
        global batch_b
        batch_b=[]
        global batch_c
        batch_c=[]
        if count == 1:
            batch_a.append(Std_records[0])
        elif count == 2:
            batch_a.append(Std_records[0])
            batch_b.append(Std_records[1])
        else:
            a=int(count/3)
            for i in range (0,a):
                batch_a.append(Std_records[i])
            for i in range (a,(2*a)):
                batch_b.append(Std_records[i])
            for i in range((2*a),count):
                batch_c.append(Std_records[i])        

print("\t\t\tWELCOME TO STUDENT MANNAGEMENT SYSTEM")
while(1):
    print(' Press 1 to Insert Record\n Press 2 to display\n Press 3 to display batches\n Press 4 to EXIT')
    choice = int(input())
    if(choice == 1):
        name = input('Enter Your Name: ')
        Prn = int(input('Enter your Prn: '))
        gender = input('Enter Male\Female: ')
        obj=std_rec(name,Prn,gender)
        obj.insert()

    elif(choice == 2):
        obj=std_rec(name,Prn,gender)
        obj.display()

    elif(choice == 3):
        obj=std_rec(name,Prn,gender)
        obj.batch()
        print("Batch a:\t",batch_a,"\nBatch b:\t",batch_b,"\nBatch c:\t",batch_c)
                    
    elif(choice == 4):
        print('THANKYOU..')
        break

    else:
        print('Invalid Choice')