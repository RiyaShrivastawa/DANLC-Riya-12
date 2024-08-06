def copy_file_contents(source_file, destination_file):
    source = open(source_file, 'r')
    content = source.read()
    source.close()
    destination = open(destination_file, 'w')
    destination.write(content)
    destination.close()

    print(f"Contents of {source_file} have been copied to {destination_file}.")

source_file = input("Enter the source file path: ")
destination_file = input("Enter the destination file path: ")

copy_file_contents(source_file, destination_file)
