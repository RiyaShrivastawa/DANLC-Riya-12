def display_words(filename):
    file = open(filename, 'r')
    for line in file:
        words = line.split()
        for word in words:
            if len(word) < 4:
                print(word)
    file.close()
display_words("story.txt")