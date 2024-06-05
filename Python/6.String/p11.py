# 11. Splitting strings with split()
"""
In Python, the split() method is used to split a string into a list of substrings based on a specified separator. It returns a list of substrings separated by the specified delimiter.

The split() method does not modify the original string; it returns a new list of substrings.
If the separator is not found in the string, the entire string is returned as a single-element list.
The split() method is commonly used for parsing and tokenizing strings, especially in text processing and data manipulation tasks.
"""
# str.split(sep=None, maxsplit=-1)

text = "Hello, World!"
words = text.split(",")  # Splitting based on comma (",")
print(words)  # Output: ['Hello', ' World!']


# Using Whitespace as Separator:
text = "Hello World!"
words = text.split()  # Splitting based on whitespace
print(words)  # Output: ['Hello', 'World!']


# Limiting the Number of Splits:
text = "one two three four five"
words = text.split(" ", 2)  # Splitting based on space, maximum 2 splits
print(words)  # Output: ['one', 'two', 'three four five']

# Handling Empty Strings:
text = "one,,two,,three"
words = text.split(",")
print(words)  # Output: ['one', '', 'two', '', 'three']

