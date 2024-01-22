"""
Write a Python code to find the occurrence of each element in a list and print the element with the highest occurrence.
"""
my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 10, 12, 2, 1]
result = []
for i in my_list:
    if i not in result:
        result.append(i)

highest_occ_element = 0
highest_occurence = 0
for i in result:
    c = my_list.count(i)
    print(f"{i} occurs {c} times")
    if c > highest_occurence:
        highest_occurence = c
        highest_occ_element = i
print(f"Element {highest_occ_element} occured maximum {highest_occurence} times")
