# 8. Write a program to find Armstrong number or not.

# Using Dynamic input
def amstrongNumber(num):
    lenngth = len(num)
    sum = 0
    for i in num:
        sum += int(i)**lenngth
        
    if int(num)==sum:
        print(f"The number {num} is Amstrong..")
    else:
        print(f"The number {num} is Not an Amstrong..")

num = input("Enter the Number :: ")
amstrongNumber(num)

# Amstrong in Range

for i in range(1,1000):
    st = str(i)
    le = len(st)
    sum = 0

    for j in st:
        sum += int(j)**le

    if sum == i:
        print(i)