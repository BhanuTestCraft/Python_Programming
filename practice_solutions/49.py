"""
Write a program to calculate the sum of all the numbers divisible by 4 from 20 to 50.
"""
sum = 0
num = 20
while num <= 50:
    if num % 4 == 0:
        sum += num
    num += 1
print(f"sum of numbers divisible by 4 is {sum}")
