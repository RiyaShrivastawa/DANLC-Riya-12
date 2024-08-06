def find_binary(number):
    binary_digits = []

    while number > 0:
        remainder = number % 2
        binary_digits.append(remainder)
        number = number // 2
    binary_digits.reverse()
    binary_string = ''.join(map(str, binary_digits))

    return binary_string
number = int(input("Enter a number: "))
binary_representation = find_binary(number)
print(f"The binary representation of {number} is: {binary_representation}")


