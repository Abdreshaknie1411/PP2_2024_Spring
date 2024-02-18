def even_numbers(n):
    for num in range(n+1):
        if num%2==0:
            yield num
def main():
    n=int(input())
    even_number=even_numbers(n)
    print(",".join(map(str,even_number)))
if __name__=="__main__":
    main()
