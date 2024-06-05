# 18. Write a program to remove the duplicate elements and return the new array

def remove_duplicete(arr):
    uniq = list(set(arr))
    return uniq

arr = [1,2,3,4,5,6,7,6,5,4,3,45,7,8]
newValue = remove_duplicete(arr)
print(newValue)