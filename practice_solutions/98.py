"""
Make your own list. Count how many numbers are divisible by both 2 and 5 in that list
"""
my_list = [2, 5, 3, 10, 20, 50, 15, 4]
count = 0
# Iterate by index.
# for i in range(0, len(my_list)):
#     if my_list[i] % 2 == 0 and my_list[i] % 5 == 0:
#         count += 1
# print(f"Numbers divisible by both 2 and 5 are {count}")

# Iterate by value
for i in my_list:
    if i % 2 == 0 and i % 5 == 0:
        count += 1
print(f"Numbers divisible by both 2 and 5 are {count}")
