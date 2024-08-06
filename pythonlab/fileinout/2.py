def count_words_in_file(filename):
    file = open(filename, 'r')
    word_count = 0
    for line in file:
        words = line.split()
        word_count += len(words)
    file.close()
    print(f"Total number of words: {word_count}")
count_words_in_file("ABC.txt")