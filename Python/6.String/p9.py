# 9. Trimming strings with strip()
"""
In Python, the strip() method is used to remove leading and trailing whitespace characters (spaces, tabs, newlines) from a string. It returns a new string with whitespace removed from both ends.
"""

# Syntax:
# str.strip([chars])

str = " Hello  !   "

striped_str1 = str.strip()
print(striped_str1)

left_striped = str.lstrip()
print(left_striped)

right_striped = str.rstrip()
print(right_striped)

# strip with Custom Character
str1 = "_Hello_ Welcome__"
striped = str1.strip('_')
print(striped)