# 17. Write a method to verify if the array contains two specified elements(12,23)

def element_contains(arr,ele1,ele2):
    return ele1 in arr and ele2 in arr

arr = [2,32,23,45,12,45,67,76]
print(element_contains(arr,12,23))

print(element_contains(arr,22,23))
