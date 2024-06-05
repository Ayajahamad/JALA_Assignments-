# 8. Write a function to find the minimum and maximum value of an array

def min_max_ofArray(arr):
    minimum = min(arr)
    maximum = max(arr)

    print(f"Minimum value in {arr} is : {minimum}")
    print(f"Maximum value in {arr} is : {maximum}")

arr = [1,2,3,4,5,6,7]
min_max_ofArray(arr)