# 1. Write a function for arithmetic operators(+,-,*,/)



def arithmeticOperators(a,b,operator):
    if operator == "+":
        print(f"Addition of {a}+{b} = {a+b}")
    if operator == "-":
        print(f"Substraction of {a}-{b} = {a-b}")
    if operator == "+":
        print(f"Multiplication of {a}*{b} = {a*b}")
    if operator == "+":
        print(f"Division of {a}/{b} = {a/b}")

a = int(input("Enter a First Number : "))
b = int(input("Enter a Second Number : "))
ope = input("Enter Operator (+,-,*,/) : ")

arithmeticOperators(a, b, ope)