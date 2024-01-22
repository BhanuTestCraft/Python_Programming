def simple_interest(x: int, y: int, z: int):
    si = (x * y * z) / 100
    return si


p = int(input("Enter the value of principal amount = "))
r = int(input("Enter the value for rate of interest = "))
t = int(input("Enter the value for time period in years = "))


interest = simple_interest(p, r, t)
print(
    f"simple intrest for amount {p}Rs for duration {t}years and with rate of interest {r}% is = {interest}"
)
