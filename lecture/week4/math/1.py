import math 
def radian(degree):
    degree_radian=math.pi*(degree/180)
    return degree_radian
degree=int(input("Input degree: "))
x_radian=radian(degree)
print(f"Output radian: {x_radian: .6f}")