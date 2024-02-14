mytext=str(input())
summ=0
for char in mytext:
    if mytext[char]>'0' and mytext[char]<'9':
        summ+=mytext[char]
print(int(summ))
