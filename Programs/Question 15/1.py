# Python Program to Find Sum of Array
my_list = [1, 2, 3, 4, 5]

# iteration using index.
sum = 0
for i in range(len(my_list)):
    sum += my_list[i]
print(sum)

# Iteration using value.
sum = 0
for value in my_list:
    sum += value
print(sum)

# using enumerate.
sum = 0
for index, value in enumerate(my_list):
    sum += value
print(sum)
