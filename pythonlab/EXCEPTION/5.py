def parse_file(file_path):
    numbers = []

    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                try:
                    number = float(line.strip())
                    numbers.append(number)
                except ValueError:
                    print(f"Error on line {line_number}: '{line.strip()}' is not a valid number.")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied to access the file '{file_path}'.")
    return numbers
file_path = input("Enter your file path")
numbers = parse_file(file_path)
print("Parsed numbers:", numbers)