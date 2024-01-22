"""
Remove all the even numbers from the list.
"""
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# new_list = []
# for i in range(0, len(my_list)):
#     if my_list[i] % 2 != 0:
#         new_list.append(my_list[i])
# print(new_list)

for i in my_list:
    if i % 2 == 0:
        my_list.remove(i)
print(my_list)
