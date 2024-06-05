# 9. Write a program to find the prime or not.

# With Dynamic input
def primeNumber(num):
    div = 0

    for i in range(1, num+1):
        if num%i == 0:
            div+=1
    if div == 2:
        print(f"{num} is a prime Number")
    else:
        print(f"{num} is not a prime Number")

num = int(input("Enter the number :: "))
primeNumber(num)

# Prime number in a Range 1-1000

for i in range(1,1001):
    sum = 0
    for j in range(1,i+1):
        if i%j == 0:
            sum+=1
        
    if sum == 2:
        print(i)
