import re 
def ddd(string):
    pattern=r"[a-z]@gamil\.+[a-z]"
    if re.fullmatch(pattern,string):
        return False
    else:
        return True
string=str(input())
print(ddd(string))