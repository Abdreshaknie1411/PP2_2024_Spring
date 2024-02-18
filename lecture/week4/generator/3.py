def divided(n):
    for num in range(n):
        if num%4==0 and num%3==0:
            yield num
def main():
    n=int(input())
    divided_num=divided(n)
    print(" ".join(map(str,divided_num)))
if __name__=="__main__":
    main()