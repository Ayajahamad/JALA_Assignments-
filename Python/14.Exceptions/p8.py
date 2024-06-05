# 8. Write a program to generate Arithmetic Exception

def generate_value_error():
    number = int("hello")

def main():
    try:
        generate_value_error()
    except ValueError:
        print("Error: Could not convert string to integer!")

# Main block
if __name__ == "__main__":
    main()

