# Python Program to Check Armstrong Number.
def is_armstrong(num):
    num_str = str(num)
    n = len(num_str)
    result = 0
    for digit in num_str:
        result = result + int(digit)**n
    if result == num:
        return True
    else:
        return False
num = int(input("Enter the value of number is : "))
print(is_armstrong(num))

