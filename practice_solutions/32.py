"""
Ask 4 numbers from user. Make sure all the numbers entered by user are different. Print which number is the smallest.
"""
num1 = float(input("Enter number 1= "))
num2 = float(input("Enter number 2= "))
while num2 == num1:
    print("Error: Please enter a different number for the second input.")
    num2 = float(input("Enter number 2= "))
num3 = float(input("Enter number 3= "))
while num3 == num1 or num3 == num2:
    print("Error: Please enter a different number for the third input.")
    num3 = float(input("Enter number 3= "))
num4 = float(input("Enter number 4= "))
while num4 == num1 or num4 == num2 or num4 == num3:
    print("Error: Please enter a different number for the fourth input.")
    num4 = float(input("Enter number 4= "))
if num1 < num2 and num1 < num3 and num1 < num4:
    print("num1 is the smallest")
elif num2 < num1 and num2 < num3 and num2 < num4:
    print("num2 is the smallest")
elif num3 < num1 and num3 < num2 and num3 < num4:
    print("num3 is the smallest")
else:
    print("num4 is the smallest")
