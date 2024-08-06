def find_duplicates(items):
    duplicates = []
    seen = set()

    for item in items:
        if item in seen:
            if item not in duplicates:
                duplicates.append(item)
        else:
            seen.add(item)

    return duplicates
numbers = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    numbers.append(element)
duplicates = find_duplicates(numbers)
print("The duplicate values in the list are:", duplicates)