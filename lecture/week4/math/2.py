
class trapezoid:
    def __init__(self,heigth,value1,value2):
        self.heigth=heigth
        self.value1=value1
        self.value2=value2
    def area(self):
        return ((self.value1+self.value2)/2)*self.heigth
p=trapezoid(int(input("Heigth: ")),int(input("Value1: ")),int(input("Value2: ")))
print("Output: ",p.area())