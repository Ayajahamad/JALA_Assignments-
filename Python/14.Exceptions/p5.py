# 5. Write a program to throw exception with your own message.

class CustomError(Exception):
    def __init__(self, message):
        self.message = message

def validate_input(value):
    if value < 0:
        raise CustomError("Input value must be non-negative.")

def main():
    try:
        # Prompt the user for input
        number = float(input("Enter a non-negative number: "))

        # Validate the input
        validate_input(number)

        # If input is valid, print it
        print("Valid input:", number)

    except ValueError:
        print("Error: Please enter a valid number.")
    except CustomError as e:
        print(f"Error: {e.message}")

# Main block
if __name__ == "__main__":
    main()
