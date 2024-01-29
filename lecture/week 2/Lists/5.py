#fuction "append"
thelist=["KBTU","NU","ALT"]
thelist.append("AITU")
print("1=", thelist)#артына косу

#fuction "extend"
thelist=["apple","orange","cherry"]
seclist=["banana","papaya"]
thelist.extend(seclist)
print("2=", thelist)#


#fuction "remove"
thelist=["apple","banana","cherry"]
thelist.remove("apple")
print("3=", thelist)#удалить


#fuction "pop"
thelist=["apple","banana","chery"]
thelist.pop(0)#удалить
print("4=", thelist)

#fuction "del"
thelist=["apple","banana","chery"]
del thelist[0]
print("5=", thelist)

#fuction "clear"
thelist=["apple","banana","chery"]
thelist.clear()
print("6=", thelist)