"""
Create a list and prompt the user for an 'old number' followed by a 'new number.' If the 'old number' exists in the list, replace it with the 'new number' provided by the user.
"""
my_list = [5, 10, 15, 20, 15]
old_num = int(input("Enter the old number= "))
new_num = int(input("Enter the new number= "))
for i in range(0, len(my_list)):
    if my_list[i] == old_num:
        my_list[i] = new_num
print(my_list)
