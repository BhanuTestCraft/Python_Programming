"""
Write a program that prompts the user to specify the length of a list and then requests numbers to populate that list. Display the fi nal list as the output.
"""
my_list = []
list_size = int(input("Enter the length of list= "))
for i in range(0, list_size):
    my_list.append(int(input(f"Enter the number at index {i}= ")))
print(my_list)
