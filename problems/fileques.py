#  file handling with exception
try:
    with open('date.ext','r') as f:
        content=f.read()
        print(content)
except FileNotFoundError:
    print("File not find")
finally:
    print("program finished")

# zero division error
def divide(x,y):
    try:
        result=x/y
        print("result", result)
    except ZeroDivisionError:
        print("cannot divide ")


divide(10,20)      
print(divide)

# validate integer input give value error
i=int(input("Enter the given:"))
