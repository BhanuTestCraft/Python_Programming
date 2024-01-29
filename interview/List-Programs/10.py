# ython Program to Find Largest Number in a List.

my_list = [10,20,45,7,17,2,33]
def largest_element_list(my_list):
    largest = 0
    for value in my_list:
        if value>largest:
            largest = value
    return largest
result = largest_element_list(my_list)
print(f"The largest element in the list is : {result}")

def largest_element_list(my_list):
    my_list.sort()
    largest = my_list[-1]
    return largest
result = largest_element_list(my_list)
print(f"The largest element in the list is : {result}")