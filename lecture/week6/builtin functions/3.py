def polindrom(s):
    s=s.replace(" ","").lower()
    return s==s[::-1]
    

s=str(input())
pol=polindrom(s)

if pol:
    print("Polindrom")
else:
    print("not polindrom")