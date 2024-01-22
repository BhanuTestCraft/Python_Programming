"""
Write a program that swaps the first and last elements of a given list.
"""
my_list = [32, 10, "Bhanu", 55.90, "xyz"]
temp = my_list[0]
my_list[0] = my_list[-1]
my_list[-1] = temp
print(my_list)
