"""
Make a program that takes a list of integers and returns the product of all the elements.
"""
my_list = [1, 2, 3, 4, 5]
product = 1
for i in my_list:
    product *= i
print(f"product of all numbers in list is {product}")
