# 12. Write a method to remove duplicate elements from an array

# using set() method
arr = [1,2,3,4,5,6,7,8,4,5,6,2,3,1]

uniq = set(arr)
arr1 = list(uniq)

print(arr1)


# using Custom method
arr2 = [1,2,3,4,5,6,7,8,7,6,5,4,3,21,1]
uniqArr = []

for i in arr2:
    if i not in uniqArr:
        uniqArr.append(i)

print(uniqArr)