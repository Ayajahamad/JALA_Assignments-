"""
1. Create a Dictionary with at least 5 key value pairs of the Student ID and Name
1.1. Adding the values in dictionary
1.2. Updating the values in dictionary
1.3. Accessing the value in dictionary
1.4. Create a nested loop dictionary
1.5. Access the values of nested loop dictionary
1.6. Print the keys present in a particular dictionary
1.7. Delete a value from a dictionary
"""

student_dict = {
    101: "John",
    102: "Alice",
    103: "Bob",
    104: "Emma",
    105: "Michael"
}
print(f"The Actual Dictionary : \n {student_dict}")

# 1.1. Adding the values in dictionary
student_dict[106] = "Henry"
print(f"Dictionary After Adding the value : \n {student_dict}")

# 1.2. Updating the values in dictionary
student_dict[101] = "Jhon Berry"
print(f"Dictionary After Updating the value : \n {student_dict}")

# 1.3. Accessing the value in dictionary
name = student_dict[101]
print(f"Accessing the Value of [101] Id : {name}")

# 1.4. Create a nested loop dictionary
student_dict["nested_dict"] = {
    'A': {'x': 1, 'y': 2},
    'B': {'x': 3, 'y': 4}
}
print(f"Dictionary After Adding Nested Dict : \n {student_dict}")

# 1.5. Access the values of nested loop dictionary
nested_value = student_dict["nested_dict"]["A"]['x']
print(f"Access the values of nested loop dictionary : {nested_value}")

# 1.6. Print the keys present in a particular dictionary
key = student_dict.keys()
print(key)

# 1.7. Delete a value from a dictionary
del student_dict[101]
print(f"After Deleting The first Key [101] : {student_dict}")