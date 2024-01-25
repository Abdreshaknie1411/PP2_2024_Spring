'''
One more value, or object in this case, evaluates to False, 
and that is if you have an object that is made from a class with a __len__ function that returns 0 or False
'''

class myWork():
    def __len__(self):
        return 0 #False

myJob=myWork()
print(bool(myJob))

#2 Function
def myLab():
    return True

print(myLab())


#3 Fuction for example
def myfuction():
    return True

if myfuction():
    print("YES")
else:
    print("NO")