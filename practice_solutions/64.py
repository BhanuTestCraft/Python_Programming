"""
Calculate factorial of a number entered by user.
"""
num = int(input("Enter the number: "))
result = 1
for i in range(num, 0, -1):
    result = result * i
print(f"factorial of the number is {result}")
