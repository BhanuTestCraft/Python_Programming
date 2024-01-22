# requirement: we need to create one list not manually.

# Method-1
# my_list = []
# for i in range(1, 21):
#     my_list.append(i)
# print(my_list)

# Method-2
# my_list = [i for i in range(1, 21)]
# new_list = [i + 6 for i in range(1, 21)]
# print(my_list)
# print(new_list)

# i=1 ODD
# i=2 EVEN
# i=3 ODD
# i=4 EVEN
# my_list = ["EVEN" if i % 2 == 0 else "ODD" for i in range(1, 21)]
# print(my_list)

# create one list having only even numbers
# my_list = [i for i in range(1, 31) if i % 2 == 0]
# print(my_list)

# ask start number, stop number and in that add only those number which are divisible by 2 and 3
start = int(input("Enter the start number= "))
stop = int(input("Enter the stop number= "))
my_list = [i for i in range(start, stop + 1) if i % 2 == 0 and i % 3 == 0]
print(my_list)
