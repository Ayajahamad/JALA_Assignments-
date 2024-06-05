# 5. Write a function to remove a specific element from an array

# using remove() method
def remove_array_element(arr,ele):
    print(f"Before Removing {arr}")
    arr.remove(ele)
    print(f"After removing {arr}")

arr = [1,2,3,4,5]
remove_array_element(arr,3)
remove_array_element(arr,1)

# using array index pop()
def remove_array_element_withindex(arr,ind):
    print(f"Before Removing {arr}")
    arr.pop(ind)
    print(f"After removing {arr}")

arr1 = [1,2,3,4,5]
remove_array_element_withindex(arr1,3)
remove_array_element_withindex(arr1,1)
