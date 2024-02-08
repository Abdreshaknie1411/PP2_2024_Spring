def summ(arr):
    sum1=0
    sum2=0

    for num in arr:
        if num>0:
            sum1+=num
        elif num<0:
            sum2+=num
    return sum1,sum2
list_arr =[]
n=int(input())
for i in range(n):
    arr=int(input())
    list_arr.append(arr)
sum1,sum2=summ(list_arr)
print(sum1)
print(sum2)