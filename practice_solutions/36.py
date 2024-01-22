"""
Take three numbers as input from User and print which one is greater or are they equal.
"""
num1 = float(input("Enter the number 1 = "))
num2 = float(input("Enter the number 2 = "))
num3 = float(input("Enter the number 3 = "))
if num1 > num2 and num1 > num3:
    print("num1 is the greatest number")
elif num2 > num1 and num2 > num3:
    print("num2 is the greatest number")
elif num3 > num1 and num3 > num2:
    print("num3 is the greatest number")
else:
    print("All the three numbers are equal")
