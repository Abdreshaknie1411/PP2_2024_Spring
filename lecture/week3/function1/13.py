import random
def myFirstGame():
    cnt=0
    needToFind=random.randint(1,20)
    name=str(input(("Hello! What is your name?\n")))
    print("Well,'{}',I am thinking of a number between 1 and 20. Take a guess.".format(name))

    while True:
        num=int(input("Take a guees.\n"))
        cnt +=1
        if num>needToFind:
            print("It is too high.Take a guess again")
        elif num<needToFind:
            print("It is too low.Take a guess again")
        else:
            print("You find this number after {} attemps. This num is {}".format(cnt,needToFind))
            break
myFirstGame()

