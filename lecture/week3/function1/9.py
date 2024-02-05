import math

def Radius(radius):
    ball_radius=3/4*math.pi*radius**3
    return ball_radius

radius=float(input())
result=Radius(radius)
print(f"{result:.2f}")

