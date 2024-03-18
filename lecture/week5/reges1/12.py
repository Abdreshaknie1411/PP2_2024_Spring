import re 
def ddd(s):
    x=r"^\S+@\S+\.\S+$"
    if re.fullmatch(x,s):
        return True
    else:
        return False
s=str(input())
print(ddd(s))