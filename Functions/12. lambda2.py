"""
Take a argument which will be a number
make a list from 0 to N
"""

make_list = lambda n: [i for i in range(0, n + 1)]

list1 = make_list(5)
list2 = make_list(10)
print(f"{list1=}")
print(f"{list2=}")
