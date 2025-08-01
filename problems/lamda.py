# write a lambda fucntion to add a number
var = lambda a,b: a+b
print(var(10,20))

# Write a Python program to create a function that takes one argument
def lm(n):
    return lambda x:n*x
product=lm(10)
print(product(2))

# sort a list of tuple
_marks=[("english",90),("maths",80),("chemistry",85)
               ]

_marks.sort(key=lambda x:x[1])
print(_marks)
