# 11. Write a program to generate IOException

"""
In Python, IOException is not a specific exception class like in languages such as Java. Instead, Python raises various exceptions related to input/output (I/O) operations under different circumstances. These exceptions are typically derived from the IOError class or its subclasses.

Here's an overview of common I/O-related exceptions in Python:

IOError: This is a base class for I/O-related exceptions. It may be raised for various I/O errors such as file not found, permission denied, or other input/output-related issues.
"""

def generate_io_exception():
    try:
        with open("non_existent_file.txt", "r") as file:
            data = file.read()
    except IOError:
        raise IOError("Input/output operation failed!")

def main():
    try:
        generate_io_exception()
    except IOError as e:
        print("Error:", e)

# Main block
if __name__ == "__main__":
    main()
