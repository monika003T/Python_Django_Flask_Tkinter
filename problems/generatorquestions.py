#generate a cube using a generator
def cube__(n):
    for i in range(1, n+1):
        yield i*i*i

for x in cube__(5):
    print(x)
# random number generator

    
import random
def randomnumber(s,e):
    while True:
        yield random.randint(s,e)

x=randomnumber(4,10)
print(next(x))
print(next(x))

