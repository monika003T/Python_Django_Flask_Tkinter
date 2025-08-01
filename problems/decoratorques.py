def dec(func):
    def wrapper(*a,**ka):
        print("monika")
        var= func(*a,**ka)
        return var
    return wrapper

@dec
def asdf():
    print("Hello")

# log function and write a value
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@logger
def multiply_numbers(x, y):
    return x * y

# Usage:
multiply_numbers(10, 20)
