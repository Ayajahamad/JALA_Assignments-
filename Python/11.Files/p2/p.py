# 2. Write a program to write text to .txt file using InputStream

import io

# Simulate an input stream with some text
input_stream = io.BytesIO(b"Hello, this is a test text for InputStream.")

# Read the text from the input stream
text = input_stream.read().decode('utf-8')

# Write the text to a .txt file
with open("./p2/output.txt", "w") as file:
    file.write(text)

print("Text has been written to output.txt")
