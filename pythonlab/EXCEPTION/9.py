import logging
logging.basicConfig(filename='error_log.txt', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def read_and_log(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        logging.error(f"File not found: '{file_path}'")
        print(f"Error: The file '{file_path}' was not found.")
    except PermissionError:
        logging.error(f"Permission denied: '{file_path}'")
        print(f"Error: Permission denied to access the file '{file_path}'.")
    except Exception as e:

        logging.error(f"Unexpected error occurred: {e}")
        print(f"Unexpected error: {e}")
file_paths = ["example.txt", "restricted_file.txt",  "valid_file.txt" ]

for path in file_paths:
    read_and_log(path)