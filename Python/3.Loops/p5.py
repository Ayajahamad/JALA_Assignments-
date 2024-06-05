# 5. Write a program to print largest number among three numbers.

def largestNumber(a,b,c):
    if a>=b and a>=c:
        largest = a
    elif b>=a and b>=c:
        largest = b
    else:
        largest = c
    print(f"Largest Among {a},{b} and {c} is : {largest}")

a = int(int(input("Enter first number :: ")))
b = int(int(input("Enter second number :: ")))
c = int(int(input("Enter third number :: ")))

largestNumber(a,b,c)
    
    