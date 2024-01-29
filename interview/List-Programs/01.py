# Python program to interchange first and last elements in a list.
my_list=[1,2,3,4,5]

# Method 1:
# size=len(my_list)
# temp = my_list[0]
# my_list[0]=my_list[size-1]
# my_list[size-1]=temp
# print(my_list)

# Method 2:
def swapList(my_list):
    size=len(my_list)
    temp = my_list[0]
    my_list[0]=my_list[size-1]
    my_list[size-1]=temp
    return my_list

result = swapList(my_list)
print(f"The string after swapping first and last value is : {result}")

# Method 3:
def swapList(my_list):
    my_list[0],my_list[-1]=my_list[-1],my_list[0]
    return my_list

result = swapList(my_list)
print(f"The string after swapping the first and last value is : {result}")