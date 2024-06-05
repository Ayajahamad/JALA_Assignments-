# 2. Write a function to calculate the average value of an array of integers

def avg_of_Array(arr):
    total = sum(arr)
    length = len(arr)

    avg = total/length
    print(f"Average of {arr} is : {avg}")

arr = [1,2,3,4,5]
avg_of_Array(arr)