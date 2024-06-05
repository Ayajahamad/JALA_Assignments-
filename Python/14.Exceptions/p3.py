# 3. Write a method which throws exception, Call that method in main class without try block

class ExampleClass:
    def divide(self, numerator, denominator):
        # This will throw ZeroDivisionError if denominator is zero
        return numerator / denominator

# Main block
if __name__ == "__main__":
    example = ExampleClass()
    # Call the method without a try block
    result = example.divide(10, 0)
    print("Result:", result)
