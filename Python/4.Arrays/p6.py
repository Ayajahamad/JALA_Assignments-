# 6. Write a function to copy an array to another array

# Using the list's copy method
def copy_array(source_array):
    new_array = source_array.copy()  
    return new_array

original_array = [1, 2, 3, 4, 5]
copied_array = copy_array(original_array)
print("Original array:", original_array) 
print("Copied array:", copied_array)      


# Using Slicing
def copy_array(source_array):
    new_array = source_array[:]
    return new_array

original_array = [1, 2, 3, 4, 5]
copied_array = copy_array(original_array)
print("Original array:", original_array)  
print("Copied array:", copied_array)      


# Extending arr with arr1
arr = [1,2,3,4,5]
arr1 = [6,7,8,9]

arr.extend(arr1)
print(arr)