"""
Write a Python program to swap the values of two variables without using a temporary variable.
"""
# Method1: using a third variable.
# a=10
# b=5
# c=a
# a=b
# b=c
# print(a)
# print(b)

# Method2: Without using third variable.
a = 5
print(f"value of a before swapping is {a}")
b = 20
print(f"value of b before swapping is {b}")
a = a + b
b = a - b
a = a - b
print(f"value of a after swapping is {a}")
print(f"value of b after swapping is {b}")
