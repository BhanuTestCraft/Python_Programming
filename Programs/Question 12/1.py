"""
Python program to interchange first and last elements in a list.
"""


def swapList(my_list: list):
    temp = my_list[0]
    my_list[0] = my_list[-1]
    my_list[-1] = temp
    return my_list


list_length = int(input("Enter the length of list = "))
orignal_list = []
for i in range(5, list_length + 1, 5):
    orignal_list.append(i)

print(f"List before interchanging the first and last element = {orignal_list}")


result = swapList(orignal_list)
print(f"List after interchanging the first and last element = {result}")
