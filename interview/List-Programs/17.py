# Python program to print negative numbers in a list.

my_list = [12, -7, 5, 64, -14]
def negative_numbers(list):
    new_list = []
    for value in my_list:
        if value<0:
            new_list.append(value)
    return new_list
result = negative_numbers(my_list)
print(f"The list having negative numbers only is : {result}")

my_list = [12, -7, 5, 64, -14]
new_list = [i for i in my_list if i<0]
print(f"The list having negative numbers only is : {new_list}")