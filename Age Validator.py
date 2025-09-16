try:
    age=int(input("Enter your age:"))
    print(f"User age is :{age}")
    if age<0:
        raise ValueError("Age cannot be negative")
except ValueError:
    print(" Error: Please enter valid numbers.")