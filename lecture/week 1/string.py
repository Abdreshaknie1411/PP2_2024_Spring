#1 function len
x="hello world"
print(len(x))

#2 Get the first character of the string txt
txt="hello world"
x=txt[0]
print(x)

#3 Get the characters from index 2 to index 4 (llo)
txt="Hello world"
x=txt[2:5]
print(x)

#4 Return the string without any whitespace at the beginning or the end.
txt="Hello world"
x=txt.strip()
print(x)

#5 Convert the value of txt to upper case
txt="hello world"
x=txt.upper()
print(x)

#6 Convert the value of txt to lower case
txt="Hello world"
x=txt.lower()
print(x)

#7 Replace the character H with a J.
txt="Hello world"
x=txt.replace("H","J")
print(x)

#8 Insert the correct syntax to add a placeholder for the age parameter
age=36
txt="My name is Jhon and I am {}"
x=txt.format(age)
print(x)
