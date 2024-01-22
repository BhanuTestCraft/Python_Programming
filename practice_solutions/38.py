"""
Write a program that takes three numbers as input and determines the largest one using nested if-else statements. Make sure all 3 numbers entered by user are different.
"""
num1 = float(input("Enter the number 1 = "))
num2 = float(input("Enter the number 2 = "))
while num2 == num1:
    print("Error: Please enter the different value for second number= ")
    num2 = float(input("Enter the number 2 = "))
num3 = float(input("Enter the number 3 = "))
while num3 == num1 and num3 == num2:
    print("Error: Please enter the different value for third number= ")
    num3 = float(input("Enter the number 3 = "))
largest_num = num1
if num2 > largest_num:
    largest_num = num2
    if num3 > largest_num:
        largest_num = num3
        print(f"The largest number is num3 {num3}")
    else:
        print(f"The largest number is num2 {num2}")
else:
    if num3 > largest_num:
        largest_num = num3
        print(f"The largest number is num3 {num3}")
    else:
        print(f"The largest number is num1 {num1}")
