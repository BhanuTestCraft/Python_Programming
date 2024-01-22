"""
Write a program to check if the number is ODD, EVEN or Equal to Zero.
"""
num = int(input("Enter the number= "))  # 0%2 = 0
if num == 0:
    print("Number is Zero")
elif num % 2 == 1:
    print("User input number is Odd")
else:
    print("User input number is Even")
