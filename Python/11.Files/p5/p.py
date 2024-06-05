# 5. Write a program to read a file a just to a particular index using seek()

# Define the index you want to seek to
index_to_seek = 10

# Open the file in read mode
with open("./p5/ex.txt", "r") as file:
    # Move the file pointer to the specified index
    file.seek(index_to_seek)
    
    # Read the content from that index onwards
    content = file.read()
    
# Print the content read from the specified index
print(f"Content from index {index_to_seek} onwards:")
print(content)
