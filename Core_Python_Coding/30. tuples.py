# Tuples: Immutable Data Type
# Immutable means we cannot change any value i.e update, we cannot delete any value, we cannot add any value i.e insert, we cannot remove any value.

my_tuple = (5, 10, 15, 20, 25, 30, 35, 40, 45, 50)
# print(my_tuple, type(my_tuple))

# print(my_tuple[0])

# How to explain that it is immutable data type
# my_tuple[0] = 100
# print(my_tuple)
# output: TypeError: 'tuple' object does not support item assignment

# Methods:

# Count
# x = my_tuple.count(25)
# print(x)

# Index
# x = my_tuple.index(25)
# print(x)

# Iteration
# for i in my_tuple:
#     print(i)

my_list = list(my_tuple)
print(my_list)
my_list.append(100)
my_tuple = tuple(my_list)  # override operation
print(my_tuple)
