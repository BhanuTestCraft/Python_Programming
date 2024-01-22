"""
Write a program to find and print all prime numbers within a given list.
"""
my_list = [2, 3, 5, 6, 8, 7, 9, 11, 12, 13, 15, 17]
for num in my_list:
    factors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            factors += 1
    if factors == 2:
        print(num)
