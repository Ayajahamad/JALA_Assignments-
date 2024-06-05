# 5. Searching in strings using index()

# index_position = string.index(substring, start, end)

str = "Hello, World"
substr = "World"
start = 5
end = 12

indexpos = str.index(substr,start,end)
print(f"Substring found at index: {indexpos}")


# Another method
# Step 3: Perform the Search with Start Index
my_string = "Welcome to Python"
subString = "to"
startInd = 9

try:
    index_position = my_string.index(subString, startInd)
    print(f"Substring found at index: {index_position}")
except ValueError:
    print("Substring not found")


# Searching with start Index
text = "Hello, welcome to the world of Python. welcome again!"
index = text.index("welcome", 10)
print(index)  # Output: 39


