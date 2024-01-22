"""
Write a program to check if the last digit of a number is divisible by 5 or not.
"""
num = int(input("Enter the number= "))
last_digit = num % 10
print(f"The last digit of {num} is {last_digit}")
if last_digit % 5 == 0:
    print(f"The last digit of number {num} is divisible by 5")
else:
    print(f"The last digit of number {num} is not divisible by 5")
