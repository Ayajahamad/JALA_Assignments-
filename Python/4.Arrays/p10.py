# 10. Write a function to find the duplicate values of an array

def findDuplicate(arr):
    uni = []
    dup = []

    for i in arr:
        if i not in uni:
            uni.append(i)
        else:
            dup.append(i)
    print(dup)

arr = [1,2,3,4,5,4,3,4,5,6,7,3,4]
findDuplicate(arr)

