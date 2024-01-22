"""
Python Program to Check Armstrong Number
"""

num = int(input("Enter any number = "))

num_str = str(num)

num_digits = len(num_str)
sum = 0
for i in range(num_digits):
    digit = int(num_str[i])
    sum = sum + (digit**num_digits)

print(f"sum of the number is {sum}")

if sum == num:
    print(f"Enterd number {num} is an armstrong number")
else:
    print(f"Entered number is not armstrong number")
