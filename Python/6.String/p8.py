# 8. startsWith(), endsWith() and compareTo()

# Syntax :
# str.startswith(prefix[, start[, end]])

text = "Hello, World!"
startsWithHello = text.startswith("Hello")
print(startsWithHello)  # Output: True

# str.endswith(suffix[, start[, end]])
text = "Hello, World!"
endsWithWorld = text.endswith("!")
print(endsWithWorld)  # Output: True

# Comparison Operators (<, >, ==):
str1 = "hello"
str2 = "world"
result = str1 < str2
print(result)  # Output: True (because 'h' < 'w')