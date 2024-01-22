"""
Write a program that has two lists and make a new list that contains only the common elements between them without duplicates.
"""
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
new_list = []
for i in list1:
    if i in list2:
        if i not in new_list:
            new_list.append(i)

print(new_list)
