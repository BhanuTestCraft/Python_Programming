"""
Ask ‘n’ from user. Create a list of first n elements but in reverse order using slicing.
"""
my_list = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
n = int(input("Enter the number= "))
new_list = my_list[n - 1 :: -1]
print(new_list)
