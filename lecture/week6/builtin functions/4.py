import time
import math
def square_root(num):
    result=math.sqrt(num)
    return result
num=int(input())
square=square_root(num)
print(f"Square root of {num} after  miliseconds is{square:.4f}")
milliseconds=int(input())
seconds=milliseconds/1000
time.sleep(seconds)
