# 7. Write a program with finally block
def divide_numbers(x, y):
    try:
        result = x / y
        print("Result of division:", result)
    except ZeroDivisionError:
        print("Error: Division by zero!")
    finally:
        print("Finally block executed.")

# Main block
if __name__ == "__main__":
    divide_numbers(10, 2)
    print("-------------------")
    divide_numbers(10, 0)
