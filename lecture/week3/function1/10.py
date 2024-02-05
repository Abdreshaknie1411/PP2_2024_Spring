def my_list(firstlist):
    newlist=[]
    for i in firstlist:
        if i not in newlist:
            newlist.append(i)
    return newlist
firstlist=[]
n=int(input(":"))
for i in range(n):
    element=input(":")
    firstlist.append(element)
answer=my_list(firstlist)
print(answer)