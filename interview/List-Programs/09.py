# Python program to find smallest number in a list.
my_list = [10,20,25,15,5]
def smallest_list_element(my_list):
    smallest = my_list[0]
    for value in my_list:
        if value<smallest:
            smallest = value
    return smallest
result = smallest_list_element(my_list)
print(f"Smallest element in the given list is : {result}")

def smallest_list_element(my_list):
    my_list.sort()
    smallest = my_list[0]
    return smallest
result = smallest_list_element(my_list)
print(f"smallest element in the given list is : {result}")