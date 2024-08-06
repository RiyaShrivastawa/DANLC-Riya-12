def remove_newlines(s):
    return s.replace('\n', '')
input_string = "Hello,\nWorld!\nThis is a test string.\n"
cleaned_string = remove_newlines(input_string)
print("Original string:")
print(input_string)
print("\nString after removing newlines:")
print(cleaned_string)