# 4. Write a program with multiple catch blocks

def perform_operations():
    try:
        # Prompt the user for input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform basic arithmetic operations
        addition = num1 + num2
        subtraction = num1 - num2
        multiplication = num1 * num2
        division = num1 / num2

        # Display the results
        print(f"{num1} + {num2} = {addition}")
        print(f"{num1} - {num2} = {subtraction}")
        print(f"{num1} * {num2} = {multiplication}")
        print(f"{num1} / {num2} = {division}")

    except ValueError:
        print("Error: Please enter valid numbers.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

# Main block
if __name__ == "__main__":
    perform_operations()
