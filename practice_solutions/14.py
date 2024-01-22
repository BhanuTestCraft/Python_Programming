"""
Write a Python program to calculate the compound interest for a given principal, rate of interest, and time period. Ask everything from the user.
"""
p = float(input("Enter the principal amount= "))
r = int(input("Enter the rate of interest= "))
t = int(input("Enter the time period= "))
amount = p * (1 + (r / 100)) ** t
print(f"Total amount till the time period is {amount} ")
ci = amount - p
print(f"comount intrest is {ci}")
