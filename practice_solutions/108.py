"""
Generate a list of at least 10 numbers. Then, create two separate lists called 'odd' and 'even.' Put all the odd numbers from the original list into the 'odd' list, and all the even numbers into the 'even' list.
"""
my_list = []
even = []
odd = []
list_len = int(input("Enter the length of list: "))
for i in range(0, list_len):
    my_list.append(int(input(f"Enter the value at index {i}: ")))
print(f"Generated list is {my_list}")
for i in my_list:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(f"The list in which we put even number is {even}")
print(f"The list in which we put odd number is {odd}")
