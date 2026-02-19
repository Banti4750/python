# posintion arguments

# def greet_user(name):
#     print(f"hi {name} !")


# greet_user("John")

# keyword argument
def greet_user(name , age):
    print(f"hi {name} ! Your age is {age}")

greet_user(age = 30 , name = "John")

# return statement is used to exit a function and return a value to the caller. If no value is specified, it returns None by default.
def square(num):
    return num * num
result = square(5)
print(result)
