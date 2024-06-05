# 9. Write a function to reverse an array of integer values

def reverse_array(arr):
    rev = arr[::-1]
    print(rev)

arr = [1,2,3,4,5]
reverse_array(arr)

# Using Reverse method
arr.reverse()
print(arr)