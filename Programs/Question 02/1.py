"""
Given two numbers, write a Python code to find the Maximum of these two numbers.
"""
num1 = int(input("Enter the value of first number= "))
num2 = int(input("Enter the value of second number= "))

if num1 > num2:
    print(f"{num1} is the largest number from {num1} and {num2}")
elif num2 > num1:
    print(f"{num2} is the largest number from {num1} and {num2}")
else:
    print("User input numbers are equal in value")
