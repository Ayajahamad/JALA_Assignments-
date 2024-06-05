# 4. Extract a string using Substring

# substring = string[start:end]

# Basic Substring Extraction
my_string = "Hello, World!"
substring = my_string[7:12]
print(substring)  # Output: World

# Extracting from the Beginning
my_string1 = "Hello, World!"
substring1 = my_string1[:5]
print(substring1)

# Extracting Until the End
my_string2 = "Hello, World!"
substring2 = my_string2[7:]
print(substring2)

# Extracting with Negative Indices
my_string3 = "Hello, World!"
substring3 = my_string3[-6:-1]
print(substring3)

# Extracting with Step
my_string4 = "Hello, World!"
substring4 = my_string4[::2]  # Every second character
print(substring4)  # Output: Hlo ol!
