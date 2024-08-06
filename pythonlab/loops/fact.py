#Q4. Wap to print the factorial of a number.
num = int(input("Enter the number:"))
result = 1
for i in range(1,num+1):
    result *= i
print("the factorial is:",result)

