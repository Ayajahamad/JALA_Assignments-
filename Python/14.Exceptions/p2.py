# 2. Handle the Arithmetic exception using try-catch block


# This program handles a ZeroDivisionError using try-except
numerator = 10
denominator = 0

try:
    # Attempt to divide by zero
    result = numerator / denominator
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
