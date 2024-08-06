def replace_string_in_file(filename, search_string, replace_string):
    file = open(filename, 'r')
    content = file.read()
    file.close()
    modified_content = content.replace(search_string, replace_string)
    file = open(filename, 'w')
    file.write(modified_content)
    file.close()

    print(f"Successfully replaced '{search_string}' with '{replace_string}' in {filename}.")
filename = input("Enter the file path: ")
search_string = input("Enter the string to search for: ")
replace_string = input("Enter the string to replace with: ")

replace_string_in_file(filename, search_string, replace_string)