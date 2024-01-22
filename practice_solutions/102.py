"""
Make your own list. Print the largest number present in that list.
"""
my_list = [1, 2, 4, 5, 10, 13, 16, 27, 91, 66, 44]
largest = my_list[0]
# Iterate by index.
# for i in range(0, len(my_list)):
#     if my_list[i] > largest:
#         largest = my_list[i]
# print(f"The largest number in the list is {largest}")


# Iterate by value.
for i in my_list:
    if i > largest:
        largest = i
print(f"The largest number in the list is {largest}")
