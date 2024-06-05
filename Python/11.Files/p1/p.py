# 1. Write a program to read text file

# read_file.py
def read_file(file_path):
    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Read the entire file content
            content = file.read()
            # Print the file content
            print(content)
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except IOError:
        print(f"An error occurred while reading the file {file_path}.")

# Specify the path to the file
file_path = 'example.txt'

# Call the read_file function
read_file(file_path)
