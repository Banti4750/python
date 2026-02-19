age = input("Enter your age : ")
try:
    age = int(age)
    if age < 0:
        raise ValueError("Age cannot be negative")
    print(f"Your age is {age}")
    income = 1000 / age
    print(f"Your income is {income}")
except ZeroDivisionError as e:
    print(f"Error: {e}")
except ValueError as e:
    print(f"Invalid input: {e}")