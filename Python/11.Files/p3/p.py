# 3. Write a program to read a file stream

# Open the file in read mode
with open("./p3/example.txt", "r") as file:
    # Read the entire file content
    content = file.read()

# Print the content
print("File content:")
print(content)
