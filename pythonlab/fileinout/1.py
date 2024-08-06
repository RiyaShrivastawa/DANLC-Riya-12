def read_file_line_by_line(filename):
    file = open(filename, 'r')
    for line in file:
        print(line, end='')
    file.close()
read_file_line_by_line("ABC.txt")