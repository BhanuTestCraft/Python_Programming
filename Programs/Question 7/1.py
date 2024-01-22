"""
Python Program to Check Prime Number.
"""
num = int(input("Enter the number to check prime or not = "))
factors = 0
if num > 1:
    for i in range(1, num + 1):
        if num % i == 0:
            factors += 1

    if factors == 2:
        print(f"Number {num} is a prime number.")
    else:
        print(f"Number {num} is not a prime number.")
else:
    print(f"Number {num} is not a prime number.")
