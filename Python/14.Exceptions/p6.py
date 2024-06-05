# 6. Write a program to create your own exception

class CustomError(Exception):
    def __init__(self, message="Custom Error"):
        self.message = message

def example_function(x):
    if x < 0:
        raise CustomError("Input must be non-negative.")
    return x * 2

try:
    result = example_function(-5)
    print("Result:", result)
except CustomError as e:
    print("Caught Custom Error:", e.message)
