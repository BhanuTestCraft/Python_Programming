# Python program to print positive numbers in a list.
my_list = [12, -7, 5, 64, -14]
def positive_numbers(list):
    new_list = []
    for value in list:
        if value>=0:
            new_list.append(value)
    return new_list
result = positive_numbers(my_list)
print(f"The list having only the positive numbers is : {result}")

my_list = [12, -7, 5, 64, -14]
def positive_numbers(list):
    new_list = [i for i in list if i>=0]
    return new_list
result = positive_numbers(my_list)
print(f"The list having only the positive numbers is : {result}")