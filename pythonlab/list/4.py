def split_list(items, length):
    if length > len(items):
        return items, []
    first_part = items[:length]
    second_part = items[length:]
    return first_part, second_part
original_list = [1, 1, 2, 3, 4, 4, 5, 1]
length_of_first_part = 3

first_part, second_part = split_list(original_list, length_of_first_part)
print("Original list:", original_list)
print("Splitted the said list into two parts:", (first_part, second_part))