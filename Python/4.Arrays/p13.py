# 13. Write a method to find the second largest number in an array
def scnd_largest_element(arr):
    arr.sort()
    length = len(arr)
    second_large_ele = arr[length-2]
    print(f"Second largest Element in {arr} is : {second_large_ele}")


arr = [1,2,3,6,3,4,87,45,90,32,43]
scnd_largest_element(arr)
