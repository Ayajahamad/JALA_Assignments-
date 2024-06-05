# 7. Write a function to insert an element at a specific position in the array

def arrInsertion(arr,position,ele):
    if position < 0 or position > len(arr):
        raise IndexError("Position out of bounds")
    else:
        arr.insert(position,ele)
        print(arr)

arr = [1,2,4,5,6]
arrInsertion(arr,2,3)

arr1 = [5,6,8,9,10]
arrInsertion(arr1,2,10)