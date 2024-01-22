"""
1. without parameters,without return
2. with parameters,without return
3. without parameters,with return
4. with parameters,with return
"""


def addition(n1, n2):
    # n1,n2: Parameters.
    # Here we have given two arg n1 and n2 which means whwnever anyone will call this function it is mandatory to provide the value for these arguments.
    total = n1 + n2
    print(total)


# addition()
# output: TypeError: addition() missing 2 required positional arguments: 'n1' and 'n2'

addition(5, 7)
# 5,7 are the arguments.

"""
We need to calculate the sum of values present in the list.
"""


def addition_list(x):  # x:Parameter
    total = 0
    for i in x:
        total += i
    print(f"sum of elements present in list is {total}")


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
addition_list(my_list)  # my_list=Argument
