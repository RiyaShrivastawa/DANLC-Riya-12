def count_word_occurrences(filename, search_word):
    word_count = 0
    file = open(filename, 'r')
    for line in file:
        words = line.split()
        word_count += words.count(search_word)
    file.close()
    print(f"The word '{search_word}' occurs {word_count} times in the file {filename}.")

filename = input("Enter the file path: ")
search_word = input("Enter the word to search for: ")

count_word_occurrences(filename, search_word)