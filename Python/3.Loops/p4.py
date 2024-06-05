# 4. Write a program to print the odd and even numbers.

# With dynamic Input
def Odd_or_Even_Number(num):
    if num%2 == 0:
        print(f"The number {num} is Even")
    else:
        print(f"The number {num} is Odd")

num = int(input("Enter a Number :: "))
Odd_or_Even_Number(num)

# Even Number from 1 to 20
print("----- Even Numbers ------")
for i in range(1, 21):
    if i%2 == 0:
        print(i)

# Odd Number from 1 to 20
print("----- Odd Numbers ------")
for i in range(1, 21):
    if i%2 != 0:
        print(i)
