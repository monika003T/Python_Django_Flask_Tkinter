''' grp ko represent krti h class
2. encapsulation  make a blueprint combining all properties 
3. inheritance is when derived can access the features of parent class
4. polymorphism when two function do the same work but differ by parameters

class is blueprint to create object
 be dont have consturctor so we use magic methods dundar
'''

# class class1:
    # def __init__(self): # 
        # pass
    # id=101
    # name="monika"

    # in this we are calling an initialization functionthat is wriiten in __init__ def __init__
    # obj=class1()


# multi level inheritance
class class1:
    c=10
class class2(class1):
   a=10
class class3(class2):
   b=20
obj=class3()
print(obj.a)