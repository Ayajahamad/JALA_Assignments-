# 4. Write a program to read a file stream supports random access

# Open the file in read mode
with open("./p4/output.txt", "r") as file:
    # Seek to the 5th byte in the file
    file.seek(5)
    # Read 10 bytes from the current position
    content = file.read(10)

    # Print the content read from the random position
    print("Content from position 5 to 15:")
    print(content)

    # Seek to the beginning of the file
    file.seek(0)
    # # Read the entire file content
    full_content = file.read()

    # Print the full content
    print("\nFull file content:")
    print(full_content)
