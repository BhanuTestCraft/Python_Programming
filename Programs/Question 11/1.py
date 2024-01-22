"""
Python Program for Sum of squares of first n natural numbers
"""


def sum_of_square(n: int) -> int:
    sum = 0
    for i in range(1, n + 1):
        sum += i**2
    return sum


# Taking user input
num = int(input("Enter any number = "))

# Calling the function and displaying the result
result = sum_of_square(num)
print(f"sum of square of first {num} numbers is {result}")
