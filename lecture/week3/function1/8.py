def my_list(list):
    for i in range(len(list)-1):
        if list[i]==0 and list[i+1]==0 and list[i+2]==7:
            return True
    return False
    
list=[]
n=int(input(":"))
for i in range(n):
    num=int(input(":"))
    list.append(num)

solution=my_list(list)
if solution:
    print("YES")
else:
    print("NO")