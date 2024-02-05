class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self,length):
        super().__init__()
        self.length=length
    def area(self):
        return self.length*self.length
    
shape_obj=Shape()
print(f"Area of Shape: ",shape_obj.area())
square_obj=Square(5)
print("Area of Square: ",square_obj.area())


        
