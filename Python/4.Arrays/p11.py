# 11. Write a program to find the common values between two arrays

# Using Loops
def findCommon_values(arr1,arr2):
    common = []
    for i in arr1:
        for j in arr2:
            if i==j:
                common.append(i)

    print(common)

arr1 = [1,2,3,4,5,6,9]
arr2 = [9,8,7,6,5,4,3,2,1]

findCommon_values(arr1,arr2)

# Another Method
set1 = set(arr1)
set2 = set(arr2)

common = list(set1 & set2)
print(common)