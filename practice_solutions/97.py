"""
Make your own list. Count the number of even numbers present in that list.
"""
my_list = [1, 2, 4, 5, 10, 13, 16, 27, 91, 66, 44]
count = 0
# Iterate by index
# for i in range(0, len(my_list)):
#     if my_list[i] % 2 == 0:
#         count += 1
# print(f"Count of even numbers present in the list is {count}")

# Iterate by value
for i in my_list:
    if i % 2 == 0:
        count += 1
print(f"Count of even numbers present in the list is {count}")
