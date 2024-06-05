# 1. Write a function to add integer values of an array

def sum_of_array(arr):
    sum = 0
    for i in arr:
        sum+=i
    print(f"Sum of {arr} is : {sum}")


arr = [1,2,3,4,5]
sum_of_array(arr)



# Using Built in method
arr1 = [1,2,3,4,5]
sum = sum(arr1)
print("Sum of array is : ",sum)
