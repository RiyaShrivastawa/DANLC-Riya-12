file1 = input("Enter your file path")

try:
    with open(file1, 'r') as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{file1}' does not exist")