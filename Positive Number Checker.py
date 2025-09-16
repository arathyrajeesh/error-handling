try:
    num = int(input("Enter a number: "))
    if num < 0:
        raise ValueError
    print("Valid positive number")
except ValueError:
    print("Negative number")
