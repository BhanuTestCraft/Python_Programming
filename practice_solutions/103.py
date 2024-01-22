"""
Make your own list. Print the smallest number present in that list.
"""
my_list = [15, 7, 23, 4, 12, 10, 5]
smallest = my_list[0]
for i in range(0, len(my_list)):
    if my_list[i] < smallest:
        smallest = my_list[i]
print(f"The smallest number in the list is {smallest}")
