def compare_numbers(a, b):
    """
    Compare two numbers and print the smaller and larger number.
    
    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.
    """
    if a < b:
        smaller = a
        larger = b
    elif a > b:
        smaller = b
        larger = a
    else:
        print("Both numbers are equal.")
        return

    print(f"The smaller number is: {smaller}")
    print(f"The larger number is: {larger}")

# Enter the input
a = int(input("Enter First Number :: "))
b = int(input("Enter Second Number :: "))

compare_numbers(a, b)

# Output:
# The smaller number is: 10
# The larger number is: 20
