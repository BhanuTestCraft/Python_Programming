"""
Make a list of your own. And remove all the duplicates element from that list.
"""
my_list = [5, 1, "code and debug", 5, 10, 20, 5, 1, 1]
new_list = []
for i in my_list:
    if i not in new_list:
        new_list.append(i)

print(new_list)
