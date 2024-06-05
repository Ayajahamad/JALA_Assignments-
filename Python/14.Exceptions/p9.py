# 9. Write a program to generate FileNotFoundException

def generate_file_not_found_exception():
    with open("non_existent_file.txt", "r") as file:
        data = file.read()

def main():
    try:
        generate_file_not_found_exception()
    except FileNotFoundError:
        print("Error: File not found!")

# Main block
if __name__ == "__main__":
    main()
