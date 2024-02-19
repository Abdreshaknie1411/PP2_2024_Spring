import math 
def area_polygon(num_sides,sides_length):
    area=(num_sides*sides_length**2)/(4*math.tan(math.pi/num_sides))
    return area
num_sides=int(input())
sides_len=float(input())
area=area_polygon(num_sides,sides_len)
print(area)