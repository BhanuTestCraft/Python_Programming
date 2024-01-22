def cube(x):
    return x * x * x


print(cube(2))

my_list = [1, 2, 3, 4, 5, 6, 7]

# Method-1: To calculate the cube of each item in the list and store it into the new list.
# new_list = []
# for item in my_list:
#     new_list.append(cube(item))
# print(new_list)

# Method-2: same thing we can do using the map function.

# Syntax:
# new_list=list(map(function_name,item))
new_list = map(cube, my_list)
print(new_list)
# output: <map object at 0x102999d50>
# with this print we will get an map object and to get the desired result we will need to convert into the required data type i.e list.

new_list = list(map(cube, my_list))
print(new_list)


# Double all numbers using map and lambda

numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))


# Add two lists using map and lambda

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))


# Define a function that doubles even numbers and leaves odd numbers as it is.
def double_even(num):
    if num % 2 == 0:
        return num * 2
    else:
        return num


numbers = [1, 2, 3, 4, 5]
result = list(map(double_even, numbers))
print(result)
