a = int(input("Enter your first number"))
b = int(input("Enter your first number"))
try:
    div = a/b
    print("division is :",div)
except ZeroDivisionError:
    print("Division by zero is invalid")
