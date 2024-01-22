"""
Make a list. Then ask a number from user. If number exists in that list then print the position of the element else print -1.
"""
my_list = [10, 20, 30, 40, 55, 65, 75, 89, 99, 79]
num = int(input("Enter the number= "))
if num in my_list:
    print("Position of num is:", my_list.index(num))
else:
    print(-1)
