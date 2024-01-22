"""
Calculate how many numbers are divisible by 7 from 1 to 100.
"""
count = 0
n = 1
while n <= 100:
    if n % 7 == 0:
        count += 1
    n += 1
print(f"{count} numbers are divisible by 7 in the given range.")
