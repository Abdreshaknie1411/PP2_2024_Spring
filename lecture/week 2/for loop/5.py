x=int(input())
y=int(input())
for i in range(x,y+1):
    if x%2==0 and y%2==0:
        print(x)
    elif x%2!=0:
        print(y)