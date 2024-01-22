"""
Make your own list. Find the sum of all numbers divisible by 3 or 4.
"""
my_list = [2, 3, 4, 8, 9, 10, 13]
total = 0
# Iterate by index.
# for i in range(0, len(my_list)):
#     if my_list[i] % 3 == 0 or my_list[i] % 4 == 0:
#         total += my_list[i]
# print(f"sum of numbers in list divisible by either 3 or 4 is {total}")

# Iterate by value.
for i in my_list:
    if i % 3 == 0 or i % 4 == 0:
        total += i
print(f"sum of numbers in list divisible by either 3 or 4 is {total}")
