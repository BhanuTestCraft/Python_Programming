"""
Python Program to Find the Factorial of a Number
"""

# Asking the number from user.
num = int(input("Enter the value of number= "))

# declaring one variable.
result = 1

# Iterating till number and calculating the result
for i in range(num, 1, -1):
    result *= i

# print the result
print(f"factorial of {num} is {result}")
