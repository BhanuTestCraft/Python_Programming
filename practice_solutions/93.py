"""
Make your own list. Print all the even numbers present in the list.
"""
my_list = [51, 74, 25, 66, 91, 88]
# Iterating through value
# for i in my_list:
#     if i % 2 == 0:
#         print(i, end=" ")

# Iterating through the position/index.
for i in range(0, len(my_list)):
    if my_list[i] % 2 == 0:
        print(my_list[i], end=" ")
