import math
class point:
    def __init__(self,x=int(input()),y=int(input())):
        self.x=x
        self.y=y

    def show(self):
        return "point:({}, {})".format(self.x,self.y)
    def move(self, ax=int(input()),ay=int(input())):
        self.x +=ax
        self.y +=ay
        return "move point:({},{})".format(self.x,self.y)
    def dist(self,secondx=int(input()),secondy=int(input())):
        subsx=self.x-secondx
        subsy=self.y-secondy
        return math.sqrt(subsx**2+subsy**2)
p=point()
s=p.show()
print(s)
d=p.dist()
print(d)

