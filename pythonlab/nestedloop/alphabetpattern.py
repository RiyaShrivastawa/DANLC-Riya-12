def print_alphabet_pattern(rows):
    ascii_value = 65
    for i in range(rows):

        for _ in range(rows - i - 1):
            print(" ", end="")


        for j in range(i + 1):
            char = chr(ascii_value + j)
            if j == 0:
                print(char, end="")
            else:
                print(" " + char, end="")


        print()



rows = 26
print_alphabet_pattern(rows)
