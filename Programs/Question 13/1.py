"""
Python Program to Swap Two Elements in a List
"""
my_list = [5, 10, 15, 20, 25, 30]
pos1 = int(input("Enter the first index for swap = "))
if pos1 > len(my_list):
    print(f"Index error: Enter any other value for first index.")
    pos1 = int(input("Enter the first index for swap = "))
pos2 = int(input("Enter the second index for swap = "))
if pos2 > len(my_list):
    print(f"Index error: Enter any other value for second index.")
    pos2 = int(input("Enter the second index for swap = "))
while pos1 > pos2:
    print(f"Error: Enter another value for second index")
    pos2 = int(input("Enter the second index for swap = "))

print(f"List before swapping two indexes = {my_list}")
temp = my_list[pos1]
my_list[pos1] = my_list[pos2]
my_list[pos2] = temp
print(f"List after swapping indexes = {my_list}")
