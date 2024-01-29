# Python program to find second largest number in a list.
my_list = [10,20,45,67,4,33,23]
def second_largest(my_list):
    largest = 0
    second_large = 0
    for value in my_list:
        if value>largest:
            second_large = largest
            largest =value
        elif value>second_large and value != largest:
            second_large = value
    return second_large
result = second_largest(my_list)
print(f"second largest element in the list is : {result}")

def second_largest(my_list):
    my_list.sort()
    second_large = my_list[-2]
    return second_large
result = second_largest(my_list)
print(f"second largest element in the list is : {result}")