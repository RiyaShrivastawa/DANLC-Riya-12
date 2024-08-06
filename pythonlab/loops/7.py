#Q7. Wap to print all the lower case alphabets.
ascii_value = ord('a')
ascii_value_end = ord('z')
while ascii_value <= ascii_value_end:
    print(chr(ascii_value), end=',')
    ascii_value += 1
