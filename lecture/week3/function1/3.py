def solve(numheads, numlegs):
    legs_for_rabbit=4
    legs_for_chikcen=2
    num_chikcen=(numlegs-numheads*2)/(legs_for_rabbit-legs_for_chikcen)
    num_rabbit=numheads-num_chikcen

    if num_chikcen>=0 and num_rabbit>=0 and num_chikcen.is_integer()and num_rabbit.is_integer():
        return int(num_chikcen),int(num_rabbit)
    else:
        return "No solution"
numheads=35
numlegs=94
result=solve(numheads,numlegs)     
print(f"the solution is{result}")

