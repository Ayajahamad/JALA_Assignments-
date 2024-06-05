# 6. Write a program to check whether a file is having read access and write access permissions

import os

# Define the file path
file_path = "./p6/output.txt"
file_path1 = "./p6/output1.txt"

# Check if the file has read access
read_access = os.access(file_path, os.R_OK)

# Check if the file has write access
write_access = os.access(file_path1, os.W_OK)

# Print the access permissions
print(f"Read access for {file_path}: {'Yes' if read_access else 'No'}")
print(f"Write access for {file_path1}: {'Yes' if write_access else 'No'}")
