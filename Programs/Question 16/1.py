# Python Program to Find Largest Element in an Array

# method-1:
my_list = [1, 2, 3, 4, 23, 56, 90, 3, 2, 1]
largest = my_list[0]
for value in my_list:
    if value > largest:
        largest = value
print(f"The largest number in array is: {largest}")


# method-2: using sorting the list.
def largest(l: list):
    n = len(my_list)
    for i in range(n):
        for j in range(n - i - 1):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return my_list[-1]


result = largest([1, 2, 3, 4, 23, 56, 90, 3, 2, 1])
print(f"The largest number in array is: {result}")
