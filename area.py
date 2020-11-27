#to find the area and parameter of circle
class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*(self.radius**2)
    def perimeter(self):
        return 2*3.14*self.radius
r=int(input("enter radius of the circle: "))
obj=circle(r)
print("area of circle:",round(obj.area(),2)) 
print("perimeter of circle:",round(obj.perimeter(),2)) 
