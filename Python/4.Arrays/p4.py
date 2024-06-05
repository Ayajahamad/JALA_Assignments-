# 4. Write a function to test if array contains a specific value
def contains_value(arr):
    ele = int(input("Enter the element :: "))

    if ele in arr:
        print(f"Array {arr} contains : {ele}")
    else:
        print(f"Array {arr} Not contains : {ele}")

arr = [1,2,3,4,5,6]
contains_value(arr)
