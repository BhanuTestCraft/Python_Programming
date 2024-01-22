"""
Implement a python program to split a list into two equal parts using slicing. One list should contain 1st half and another list should contain 2nd half.
"""
my_list = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
list1 = my_list[: len(my_list) // 2]
list2 = my_list[(len(my_list) // 2) :]
print(list1)
print(list2)
