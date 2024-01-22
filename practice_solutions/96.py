"""
Make your own list. Print the sum of all elements present in that list.
"""
my_list = [51, 74, 25, 66, 91, 88]
sum = 0
# for i in my_list:
#     sum += i
# print(f"sum of all the elements in the list is {sum}")

# Iterate by index.
for i in range(0, len(my_list)):
    sum += my_list[i]
print(f"sum of all the elements in the list is {sum}")
