# Python Program to Find the Factorial of a Number.
def factorial(num):
    if num<0:
        return "Factorial is not defined for negative numbers"
    fact=1
    for i in range(num,0,-1):
        fact*=i
    return fact
num = int(input("Enter the value of number : "))
result = factorial(num)
print(f"The factorial of the number {num} is {result}")

def factorial(n):
    if n<0:
        return "Factorial is not defined for negative numbers"
    elif n==0 and n==1:
        return 1
    else:
        fact=1
        while n>1:
            fact*=n
            n-=1
        return fact
n = int(input("Enter the value of number : "))
result = factorial(n)
print(f"Factorial of number {n} is {result}")
    