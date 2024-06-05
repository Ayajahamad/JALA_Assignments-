# 12. Converting integer objects to Strings
"""
In Python, we can convert integer objects to strings using the str() constructor or the format() method.
"""

# Using str() Constructor:
number = 123
string_number = str(number)
print(string_number)  # Output: "123"

# Using format() Method:
# "{:d}".format(integer)
number = 456
string_number = "{:d}".format(number)
print(string_number)  # Output: "456"

