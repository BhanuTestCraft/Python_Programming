"""
Calculate how many numbers are divisible by both 6 and 7 between 1 to 200.
"""
count = 0
num = 1
while num <= 200:
    if num % 6 == 0 and num % 7 == 0:
        count += 1
    num += 1
print(f"{count} numbers are divisible by both 6 and 7")
