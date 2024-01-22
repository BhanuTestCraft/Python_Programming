# Strings---Iterable data type.
# Immutable data type.

a = "code and debug"
print(a, type(a))

# How to answer that it is immutable data type
# a[0] = "Z"
# print(a)
# output: TypeError: 'str' object does not support item assignment

# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
# print(a[-1])

# Iteration by value and index
# print every charcter in the string

# Iteration by index.
my_string = "code and debug"
# for i in range(0, len(my_string)):
#     print(my_string[i], end=" ")

# Iteration by value.
# for value in my_string:
#     print(value, end=" ")

# reverse string
for i in range((len(my_string) - 1), -1, -1):
    print(my_string[i], end=" ")
