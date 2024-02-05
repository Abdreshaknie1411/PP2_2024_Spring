class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
    
class Restangle(Shape):
    def __init__(self):
        self.lenght=float(input("length: "))
        self.width=float(input("width: "))
    def area(self):
        return self.lenght*self.width
    
Shape_obj=Shape()
print("area of shape: ",{Shape_obj.area()})
Restangle_obj=Restangle()
print("Area of restangle: ",{Restangle_obj.area()})