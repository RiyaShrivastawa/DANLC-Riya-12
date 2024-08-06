a = [1, 2, 3]
b = [4, 5, 6]
c = [[1, 2], [3, 4], [5, 6]]
merged_list = a + b
flattened_list = [item for sublist in c for item in sublist]

print("Merged list:", merged_list)
print("Flattened list:", flattened_list)
