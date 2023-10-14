# basic
def Hi(x):
    print("Hi",x)
    return 1


# # return
import math
def log(n,x):
    return math.log(x,n)
print(log(int(input("底數：")),int(input("對數："))))


# local? global?
x = 0
def f(x:int):
    x += 1
    return x+1
x = f(x)
print(x)