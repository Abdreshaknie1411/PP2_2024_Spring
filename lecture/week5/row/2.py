import re 
f=open("row.txt","r",encoding="utf8")
text=f.read()

KKM_code=r"\n.+(РНМ).*(?P<KKM>[0-9]{12})"
result=re.search(KKM_code,text)
if result:
    print(result.group('KKM'))
else:
    print("not found")