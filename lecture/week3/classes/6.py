def Prime():
    num= int(input(":"))
    size=(num//2)+1
    for i in range(2,size,1):
        if num % i ==0:
            return True
    return False
solution=Prime()
if solution:
    print("This is a prime number")
else:
    print("This is not a prime number")
    