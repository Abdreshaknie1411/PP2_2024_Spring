sum=0
sum1=0
list_arr=[]
n=int(input())
for i in range(n):
    arr=int(input())
    list.append(arr)
    if arr<0:
        sum+=arr
    elif arr>0:
        sum1=sum1+arr
print(sum)
print(sum1)


