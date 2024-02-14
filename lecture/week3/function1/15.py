class Array:
    def __init__(self):
        self.List_arr=[]
    def add_element(self,element):
        self.List_arr.append(element)
    def get__arr(self):
        return self.List_arr
    def summ(self,sum1=0,sum2=0):
        self.sum1=sum1
        self.sum2=sum2
        for num in self.List_arr:
            if num<0:
                sum1+=num
            elif num>0:
                sum2+=num
        return sum1,sum2
    def maxx(self,max1=0):
        self.max1=max1
        for num in self.List_arr:
            if num>max1:
                max1=num
        return max1
    def minn(self,min1=100):
        for num in self.List_arr:
            if num<min1:
                min1=num
        return min1


p=Array() 
n=int(input())
for i in range(n):
    element=int(input())
    p.add_element(element)
print(p.get__arr())
print(p.summ())
print(p.maxx())
print(p.minn())