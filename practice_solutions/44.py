"""
Ask start number and end number from user. Print all the numbers from
start to end using while loop.
"""
num_start = int(input("Enter the starting number: "))
num_stop = int(input("Enter the last number: "))
n = num_start
while n <= num_stop:
    print(n, end=" ")
    n = n + 1
