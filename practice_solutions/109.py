"""
Start by creating two separate lists with random numbers. Then, create a third list that merges the numbers from the first and second lists together.
"""
my_list1 = [1, 3, 5, 7, 9]
my_list2 = [2, 4, 6, 8, 10]
comb_list = []
for i in range(0, len(my_list1)):
    comb_list.append(my_list1[i])
for i in range(0, len(my_list2)):
    comb_list.append(my_list2[i])
print(f"comibine list= {comb_list}")
