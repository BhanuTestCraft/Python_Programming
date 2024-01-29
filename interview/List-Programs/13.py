# Python program to print odd numbers in a List.
my_list = [1,2,3,54,67,88,99,45,34,33]
def odd_list(my_list):
    new_list = []
    for value in my_list:
        if value%2!=0:
            new_list.append(value)
    return new_list
result = odd_list(my_list)
print(f"The list containing only the odd numbers is : {result}")

my_list = [1,2,3,54,67,88,99,45,34,33]
def odd_list(list):
    new_list = [i for i in list if i%2!=0]
    return new_list
result = odd_list(my_list)
print(f"The list containing only the odd numbers is : {result}")