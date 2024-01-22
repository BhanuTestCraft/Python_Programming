"""
Ask a number from user. Print all the numbers from 1 to that number
"""
num = int(input("Enter the number: "))
n = 1
while n <= num:
    print(n, end=" ")
    n = n + 1
