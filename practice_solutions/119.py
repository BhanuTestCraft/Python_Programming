"""
Write a program to split a given list into two halves.
"""
my_list = [1, 2, 3, 4, 5, 6]
first_half = []
second_half = []
num = int(len(my_list) / 2)
for i in range(0, num):
    first_half.append(my_list[i])
print(first_half)
for j in range(num, len(my_list)):
    second_half.append(my_list[j])
print(second_half)
