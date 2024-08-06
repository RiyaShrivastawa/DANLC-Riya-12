try:
    num1 = input("Enter the first number: ")
    if not num1.replace('.', '', 1).isdigit() and not (num1.startswith('-') and num1[1:].replace('.', '', 1).isdigit()):
        raise TypeError(f"Error: '{num1}' is not a valid numerical input.")

    num2 = input("Enter the second number: ")
    if not num2.replace('.', '', 1).isdigit() and not (num2.startswith('-') and num2[1:].replace('.', '', 1).isdigit()):
        raise TypeError(f"Error: '{num2}' is not a valid numerical input.")

    num1 = float(num1)
    num2 = float(num2)

    print(f"The numbers you entered are {num1} and {num2}.")
except TypeError as e:
    print(e)