"""
Make your own list. Print how many positive and negative numbers are here.
"""
my_list = [-1, 1, -2, 2, -3, 3, -4, 4]
# Iterate by index
# pos_num = 0
# neg_num = 0
# for i in range(0, len(my_list)):
#     if my_list[i] >= 0:
#         pos_num += 1
#     else:
#         neg_num += 1
# print(f"Positive numbers in the list are {pos_num}")
# print(f"Negative numbers in the list are {neg_num}")

# Iterate by value
pos_num = 0
neg_num = 0
for i in my_list:
    if i >= 0:
        pos_num += 1
    else:
        neg_num += 1
print(f"Positive numbers in the list are {pos_num}")
print(f"Negative numbers in the list are {neg_num}")
