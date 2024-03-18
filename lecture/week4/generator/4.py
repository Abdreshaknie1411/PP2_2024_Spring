def rangee(a,b):
    for i in range(a,b):
        c=i*i
        yield c
a=int(input())
b=int(input())
for c in range(a,b+1):
    print(c*c)