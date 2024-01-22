"""
Ask start and end index from the user. Create a list from start index to end index using slicing.
"""
my_list = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
start_index = int(input("Enter the starting index of list= "))
end_index = int(input("Enter the ending index of list= "))
new_list = my_list[start_index : (end_index + 1)]
print(new_list)
