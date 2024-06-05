# 14. Write a method to find the second largest number in an array

def sec_largest_num(arr):
    first = 0
    sec = 0

    for i in arr:
        if i>first:
            sec=first
            first=i
        elif i>sec and sec != first:
            sec = i

    # print(first)
    print(f"Second largest Number is : {sec}")

arr = [23,43,34,12,21,24,25,67,87,67,89,90]
sec_largest_num(arr)