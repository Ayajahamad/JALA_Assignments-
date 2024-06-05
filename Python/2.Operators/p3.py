# 3.  Write a program to find the two numbers equal or not.

def equalNumber(a,b):
    if a==b:
        print(f"The numbers {a} and {b} are Equal")
    else:
        print(f"The numbers {a} and {b} are Not Equal")

a = int(input("Enter First Number :: "))
b = int(input("Enter Second Number :: "))

equalNumber(a,b)
