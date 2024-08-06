def sum_list(items):
    return sum(items)

numbers = []

n = int(input("Enter the number of elements in the list: "))

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    numbers.append(element)
result = sum_list(numbers)
print("The sum of the list is:", result)