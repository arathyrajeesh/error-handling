numbers = [10, 20, 30, 40]

try:
    index = int(input("Enter an index number: "))
    print("Value at index", index, "is:", numbers[index])
except IndexError:
    print("Error: Index out of range. Please enter a valid index (0-3).")
except ValueError:
    print("Error: Please enter a valid number.")
