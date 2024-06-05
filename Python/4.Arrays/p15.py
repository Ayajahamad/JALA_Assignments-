# 15. Write a method to find number of even number and odd numbers in an array

def even_odd_numbers(arr):
    even = []
    odd = []
    for i in arr:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    print(f"Even numbers in {arr} is : {even}")
    print(f"Odd numbers in {arr} is : {odd}")

arr = [1,12,11,23,22,24,26,8,98,90,78,55,65]
even_odd_numbers(arr)
