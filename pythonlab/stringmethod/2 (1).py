def remove_duplicates(input_string):
    seen = set()
    result = []

    for char in input_string:
        if char not in seen:
           seen.add(char)
           result.append(char)

    return ''.join(result)
input_string = input("Enter the string:")
output_string = remove_duplicates(input_string)
print("Input:", input_string)
print("Output:", output_string)