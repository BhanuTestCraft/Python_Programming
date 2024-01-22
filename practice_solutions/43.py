"""
Ask a number (N) from user. Print all the numbers from N to 1.
"""
num = int(input("Enter the number: "))
n = num
while n >= 1:
    print(n, end=" ")
    n = n - 1
