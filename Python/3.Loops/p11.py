# 11. Program to check whether a number is EVEN or ODD using switch

def is_even():
    return "The number is Even"

def is_odd():
    return " The number is odd"

def is_default():
    return "Invalid input"

def check_even_odd(num):
    switch_dict = {
        0 : is_even,
        1 : is_odd
    }

    return switch_dict.get(num%2, is_default)()

num = int(input("Enter the number :: "))
print(check_even_odd(num))


"""
In Python, there is no built-in switch or case statement like you might find in languages such as C, C++, Java, or JavaScript. However, similar functionality can be achieved using a variety of methods.
"""