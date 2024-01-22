"""
Write a program to find the average of all the numbers present in the list.
"""
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for i in my_list:
    sum += i
print(f"sum of numbers in the list is: {sum}")
average = sum / len(my_list)
print(f"Average of numbers in the list is: {average}")
