"""
Python Program for Simple Interest.
SI=(p*r*t)/100
"""
# Taking input from the user.
p = float(input("Enter the value of principal amount = "))
r = float(input("Enter the value for rate of interest = "))
t = int(input("Enter the time period in years = "))

simple_interest = (p * r * t) / 100

print(
    f"simple intrest for amount {p}Rs for duration {t}years and with rate of interest {r}% is = {simple_interest}"
)
