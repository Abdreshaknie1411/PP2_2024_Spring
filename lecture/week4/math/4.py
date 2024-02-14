def area(heigth,Length_of_bace):
    area_parallelogram=heigth*Length_of_bace
    return area_parallelogram
heigth=float(input("Height of parallelogram: "))
length_of_bace=float(input("Length of base: "))
area_par=area(heigth,length_of_bace)
print("Output: ",area_par)