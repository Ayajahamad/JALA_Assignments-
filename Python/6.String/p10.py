# 10. Replacing characters in strings with replace()
"""
In Python, the replace() method is used to replace occurrences of a specified substring or characters within a string with another substring or characters. It returns a new string with the replacements applied.
- The replace() method does not modify the original string; it returns a new string with replacements applied.
"""

# str.replace(old, new[, count])
text = "Hello, World!"
new_text = text.replace("World", "Python")
print(new_text)  # Output: "Hello, Python!"

# Example (Limiting Replacements):
text = "one one two three one"
new_text = text.replace("one", "ONE", 2)
print(new_text)  # Output: "ONE ONE two three one"
