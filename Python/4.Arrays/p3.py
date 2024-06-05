# 3. Write a program to find the index of an array element

# using index() method
def arrIndex(arr):
    try:
        ele = int(input("Enter the lement :: "))
        ind = arr.index(ele)
        print(f"Index of {ele} in {arr} is :: {ind}")
    except ValueError:
        print("Element is Not in Array")

arr = [1,2,3,4,5,6]
arrIndex(arr)

# using Custom method
def arrIndex_withCustom(arr1):
    ele = int(input("Enter the Element :: "))
    for i in range(len(arr1)):
        if arr1[i] == ele:
            return f"Index of {ele} is : {i}"
    return f"Index of {ele} is Not in Array"

arr1 = [6,7,8,9,10]
print(arrIndex_withCustom(arr1))



