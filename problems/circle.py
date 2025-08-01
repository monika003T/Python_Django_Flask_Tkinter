# create a class with with builtin module
import array

from problems.oop import class2
for name in array.__dict__:
   print(name)

# create a class with namspace dispaly the name od that class
class class1:
   id=101
   
   name="monika"

print(class1.__dict__)

# CREATE A INSTANCE OF CLASS
class Students: 
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        
student = Students('12', 'Frank Gibson')
print(student.__dict__)



#BUILTINS
import builtins
help(builtins.abs)
print(builtins.abs(-155))

# function student() show argument using attribute

























































































    






















































































