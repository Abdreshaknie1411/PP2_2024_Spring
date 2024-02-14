fruits=["banana","apple","orange","kiwi"]
def function(element):
    for a in fruits:
        if a==element:
            fruits.remove(a)
            print(fruits)
function("kiwi")            
        
