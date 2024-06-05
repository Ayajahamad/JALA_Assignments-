# 10. Write a program to palindrome or not.
def palindromeCheck(inp):
    rev = inp[::-1]
    if inp == rev:
        print("Palindrome")
    else:
        print("Not a palindrome")

inp = input("Enter the input to check Palindrome :: ")
palindromeCheck(inp)