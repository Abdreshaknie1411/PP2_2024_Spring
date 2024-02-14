def minn(arr,min1=100):
    for num in arr:
        if num<min1:
            min1=num
    return min1
list_arr=[]
a=list(map(int,input().split()))
min1=minn(a)
print(min1)
