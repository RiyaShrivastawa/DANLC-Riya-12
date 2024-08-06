def cnt_char(s):
    letters = 0
    digits = 0
    special_symbols = 0

    for char in s:
        if char.alpha():
            letters += 1
        elif char.digit():
            digits += 1
        else:
            special_symbols += 1

    return letters, digits, special_symbols
input_string = "My Name is Riya@11009"
letters, digits, special_symbols = cnt_char(input_string)
print(f"Letters: {letters}")
print(f"Digits: {digits}")
print(f"Special Symbols: {special_symbols}")