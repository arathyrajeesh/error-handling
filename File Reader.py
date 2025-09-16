try:
    filename = input("Enter the filename: ")
    with open(filename, "r") as file:
        content = file.read()
        print("\nFile Content:\n")
        print(content)
except FileNotFoundError:
    print("Error: The file was not found.")
