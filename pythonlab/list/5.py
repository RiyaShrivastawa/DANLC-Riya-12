def traverse_reverse_with_indices(items):
    length = len(items)
    for i in range(length-1, -1, -1):
        print(f"Index {i}: {items[i]}")
original_list = ['red', 'green', 'white', 'black']
print("Original list:", original_list)
print("Traverse the said list in reverse order:")
traverse_reverse_with_indices(original_list)