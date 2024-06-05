# 4.  Program for relational operators (<, <==, >, >==)

def relationalOperators(a,b):
    print(f"{a} < {b}  = {a<b}")
    print(f"{a} <= {b} = {a<=b}")
    print(f"{a} > {b}  = {a>b}")
    print(f"{a} >= {b} = {a<=b}")

a = int(input("Enter First Number :: "))
b = int(input("Enter Second Number :: "))

relationalOperators(a,b)