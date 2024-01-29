# Python program to print even numbers in a list.
my_list = [1,2,34,56,73,12,45,88]
def even_list(my_list):
    new_list = []
    for value in my_list:
        if value%2==0:
            new_list.append(value)
    return new_list
result = even_list(my_list)
print(f"The list conatining only the even numbers from the given list is : {result}")

my_list = [1,2,34,56,73,12,45,88]
def even_list(list):
    new_list = [i for i in list if i%2==0]
    return new_list
result = even_list(my_list)
print(f"The list conatining only the even numbers from the given list is : {result}")