import os 
import re 
with open("123.txt")as file:
    lines=file.readline()
    for i in lines:
        result=re.findall(r"[A-Za-z]",lines)
        print(result)

