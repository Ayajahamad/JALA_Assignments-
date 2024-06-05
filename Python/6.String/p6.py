# 6. Matching a String Against a Regular Expression With matches()

import re

text = "Hello, World!"
pattern = r"Hello,.*"
match_object = re.match(pattern, text)
print(match_object)

if match_object:
    print("Match found!")
else:
    print("No match found.")

"""
    text: The string to be matched, which is "Hello, World!".
    pattern: The regular expression pattern, which matches the string starting with "Hello," followed by zero or more characters (.*).
"""

"""
'.*' : This pattern matches any sequence of characters, including an empty string.

'a.*b' : This pattern matches any string that starts with an 'a', followed by zero or more characters (.*), and ends with a 'b'. For example, it matches 'ab', 'a123b', 'abbbbb', etc.

'.*\d.*' : This pattern matches any string that contains at least one digit (\d). The .* before and after \d allow for any characters before and after the digit.

'.*\w{3}.*' : This pattern matches any string that contains a sequence of three word characters (\w{3}). The .* before and after \w{3} allow for any characters before and after the three-word characters.
"""

