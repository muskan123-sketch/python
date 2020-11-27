#to find the area of rectangle
class rectangle():
    def __init__(self,l,b):     #landb are respectively the length and breadth
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b    
l=int(input("enter the length of rectangle"))
b=int(input("enter the breadth of rectangle"))
obj=rectangle(l,b)
print("area of rectangle: ",obj.area())
|