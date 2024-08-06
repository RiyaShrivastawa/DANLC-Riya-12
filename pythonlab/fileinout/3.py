def count_uppercase_characters(filename):
    file = open(filename, 'r')
    uppercase_count = 0
    for line in file:
        uppercase_count += sum(1 for char in line if char.isupper())
    file.close()
    print(f"Total number of uppercase characters: {uppercase_count}")
count_uppercase_characters("ABC.txt")