global student
student = 0
roll_no = 0
# declaring the lists
Student_info = []
batch_a=[]
batch_b=[]
batch_c=[]

def insert_info(name,Prn,gender):
    global student
    #function to insert data into the list
    temp_list = list()
    roll_no = Prn % 100
    temp_list.append(roll_no)
    temp_list.append(Prn)
    temp_list.append(name)
    temp_list.append(gender)
    Student_info.append(temp_list)
    student = student + 1
    return 0


   
def display():
    #displaying the data in list
    if(len(Student_info)==0):
        print('Records Are Empty')
    else:
        Student_info.sort()
        for j in Student_info:
            print(j)

def batch():
    global batch_a
    batch_a=[]
    global batch_b
    batch_b=[]
    global batch_c
    batch_c=[]
    if student == 1:
        batch_a.append(Student_info[0])
    elif student == 2:
        batch_a.append(Student_info[0])
        batch_b.append(Student_info[1])
    else:
        a=int(student/3)
        for i in range (0,a):
            batch_a.append(Student_info[i])
        for i in range (a,(2*a)):
            batch_b.append(Student_info[i])
        for i in range((2*a),student):
            batch_c.append(Student_info[i])
    
while(1):
    print('Press 1 to Insert Record \n  Press 2 to Display the Data \n Press 3 to divide students into batches \n Press 4 To EXIT')
    try:
        choice = int(input())
    except:
        print('Please enter valid value')
        
    if(choice == 1):
        try:
            name = input('Enter Your Name')
            Prn = int(input('Enter your Prn'))
            gender = input('Enter your gender')
            insert_info(name,Prn,gender)
        except:
            print('INVALID DETAILS')

    

    elif(choice == 2):
        print('Displaying records...')
        display()

    elif(choice == 3):
        batch()
        print("Batch A-\n",batch_a,"\nBatch B-\n",batch_b,"\nBatch C-",batch_c)

    elif(choice == 4):
        print('Thank You')
        exit()
    else:
        print('INVALID CHOICE')
