import re 
txt=str(input())
x=re.sub(r'[A-Z][^A-Z]*'," ",txt)
print(x)