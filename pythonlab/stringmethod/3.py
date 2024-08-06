def count_characters(input_string):
    uppercase_count = 0
    lowercase_count = 0
    special_count = 0
    numeric_count = 0
    for char in input_string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            numeric_count += 1
        else:
            special_count
    return uppercase_count, lowercase_count, numeric_count, special_count

input_string = input("Enter your String:")
upper, lower, numeric, special = count_characters(input_string)

print("Input:", input_string)
print("Uppercase:", upper)
print("Lowercase:", lower)
print("Numeric:", numeric)
print("Special characters:", special)