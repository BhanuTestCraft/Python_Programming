"""
Given a list of strings, create a new list containing the lengths of each string using list comprehension.
"""
my_list = ["apple", "banana", "orange", "kiwi"]
new_list = [len(my_list[i]) for i in range(0, len(my_list))]
print(new_list)
