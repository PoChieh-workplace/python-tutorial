# basic
def Hi(x):
    print("Hi",x)
Hi(input())

# return
import math
def log(n,x):
    return math.log(x,n)
print(log(int(input("底數：")),int(input("對數："))))


# local? global?
x = 1
def xfunc(x:int):
    x += 1
    return x+1
xfunc(x)
print(x)