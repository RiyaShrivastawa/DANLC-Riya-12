def find_largest_smallest(items):
    if len(items) == 0:
        return None, None

    largest = items[0]
    smallest = items[0]
    for item in items:
        if item > largest:
            largest = item
        if item < smallest:
            smallest = item

    return largest, smallest
numbers = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    numbers.append(element)

largest, smallest = find_largest_smallest(n)
print("The largest number in the list is:", largest)
print("The smallest number in the list is:", smallest)