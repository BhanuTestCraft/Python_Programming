"""
Calculate factorial of a number entered by user.
"""
num = int(input("Enter the number: "))
factorial = 1
while num > 1:
    factorial = factorial * num
    num -= 1
print(f"factorial of the orignal number is {factorial}")
