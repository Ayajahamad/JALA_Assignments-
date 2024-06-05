# 16. Write a function to get the difference of largest and smallest value

def diff_of_largest_and_smallest(arr):
    if not arr:
        print("Array is Empty")
    else:
        large = max(arr)
        small = min(arr)

        diff = large-small
        print(f"Difference between {large} and {small} is : {diff}")

arr = [1,12,11,23,22,24,26,8,98,90,78,55,65]
diff_of_largest_and_smallest(arr)

arr = []
diff_of_largest_and_smallest(arr)