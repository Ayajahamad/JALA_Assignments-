# 3. Program to equal operator and not equal operators

a = 10
b = 20
c = 10

# Equality Check
def equalOperator(a,b,c):
    if a==b:
        print(f"{a} Equal to {b}")
    if a==c:
        print(f"{a} Equal to {c}")
    else:
        print("not Equal")

equalOperator(a,b,c)



# unEquality Check
def notEqual(a,b,c):
    if b!=a:
        print(f"{b} is Not Equal {a}")
    if b!=a:
        print(f"{b} is Not Equal {c}")
    else:
        print("Equal")
notEqual(a,b,c)
    