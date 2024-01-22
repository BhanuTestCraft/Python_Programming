"""
Ask ‘n’ from user. Create a list of last n elements but in reverse order using slicing.
"""
n = int(input("Enter the number= "))
my_list = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
new_list = my_list[-1 : -(n + 1) : -1]
print(new_list)
