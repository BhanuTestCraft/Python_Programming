# How To Find the Length of a List in Python

my_list = [1,2,3,4,5]
# Method 1:
size = len(my_list)
print(f"The length of the given list is : {size}")

# Method 2:
size=0
for v in my_list:
    size+=1
print(f"The length of the given list is : {size}")

# Method 3:
size = sum(1 for i in my_list)
print(f"The length od the given list is : {size}")