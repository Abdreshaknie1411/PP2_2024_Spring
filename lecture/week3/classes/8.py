class Shape:
    def __init__(self,hegth,wigth):
        self.hegth=hegth
        self.wigth=wigth
    def Print(self):
        return self.hegth*self.wigth
class Traingle(Shape):
    def __init__(self, a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def Print(self):
        return (self.a*self.b)/2
t =Traingle(Shape)
print(t.Print())
        