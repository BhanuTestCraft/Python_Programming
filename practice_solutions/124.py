"""
Generate a list of list using list comprehension where format should be [[1, ”ODD”], [2, “EVEN”], [3, ”ODD”]].
"""
my_list = [[i, "EVEN" if i % 2 == 0 else "ODD"] for i in range(1, 11)]
print(my_list)
