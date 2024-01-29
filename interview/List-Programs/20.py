# Python – Remove empty List from List.

my_list = [5, 6, [], 3, [], [], 9]
new_list = [i for i in my_list if i!=[]]
print(f"The list after removing the empty list from the given list is : {new_list}")

my_list = [5, 6, [], 3, [], [], 9]
def empty_list_remove(list):
    new_list = []
    for value in list:
        if value:
            new_list.append(value)
    return new_list
result = empty_list_remove(my_list)
print(f"The list after removing the empty list from the given list is : {new_list}")

my_list = [5, 6, [], 3, [], [], 9]
def empty_list_remove(list):
    while [] in list:
        list.remove([])
    return list
result = empty_list_remove(my_list)
print(f"The list after removing the empty list from the given list is : {new_list}")
