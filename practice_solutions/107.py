"""
Ask the user for a number. Then, from a list of numbers, remove all the numbers that can be divided by the number the user entered.
"""
my_list = [10, 15, 20, 25, 30]
new_list = []
num = int(input("Enter the number= "))
for i in my_list:
    if i % num != 0:
        new_list.append(i)
print(new_list)

# my_list = [10, 15, 20, 25, 30]
# num = int(input("Enter the number: "))

# # Create a copy of the list to avoid modifying it while iterating
# for i in my_list[:]:
#     if i % num == 0:
#         my_list.remove(i)

# # Print the updated list
# print(my_list)
