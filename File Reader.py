try:
    filename = input("Enter the filename: ")
    with open(filename, "r") as file:
        c = file.read()
        print("\nFile Content:\n")
        print(c)
except FileNotFoundError:
    print("Error: The file was not found.")
