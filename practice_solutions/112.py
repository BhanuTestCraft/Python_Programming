"""
Take 10 integer inputs from user and store them in a list. Now, copy all the elements in another list but in reverse order.
"""
my_list = []
for i in range(0, 10):
    my_list.append(int(input(f"Enter the number at index {i}= ")))
print(f"old list= {my_list}")
# new_list = my_list.copy()
# new_list.reverse()
# print(f"new list= {new_list}")

new_list = []
for i in range((len(my_list) - 1), -1, -1):
    new_list.append(my_list[i])
print(f"new list= {new_list}")
