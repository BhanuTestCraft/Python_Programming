"""
Implement a python program to get the last 'n' elements from a list using slicing.
"""
n = int(input("Enter the number= "))
my_list = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
new_list = my_list[-n:]
print(new_list)
