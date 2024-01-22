"""
Make your own list. Find the sum of all even numbers present in that list.
"""
my_list = [51, 74, 25, 66, 91, 88]
total = 0
# Iterate by index
# for i in range(0, len(my_list)):
#     if my_list[i] % 2 == 0:
#         total += my_list[i]
# print(f"sum of all even numbers present in the list is {total}")

# Iterate by value
for i in my_list:
    if i % 2 == 0:
        total += i
print(f"sum of all even numbers present in the list is {total}")
