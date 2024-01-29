# Reversing a List in Python.
my_list=[1,2,3,4,5]
new_list=[]

# Method 1:
def reverseList(my_list):
    size=len(my_list)
    print(f"The list before reversal is : {my_list}")
    for i in range(size-1,-1,-1):
        new_list.append(my_list[i])
    return new_list
result = reverseList(my_list)
print(f"The list after the reversal is : {result}")

# Method 2:
my_list=[1,2,3,4,5]
def reverseList(my_list):
    print(f"The list before reversal is : {my_list}")
    my_list[::-1]
    return my_list
result = reverseList(my_list)
print(f"The list after the reversal is : {result}")

# Method 3:
my_list=[1,2,3,4,5]
print(f"The list before the reversal is : {my_list}")
new_list=[my_list[i] for i in range((len(my_list)-1),-1,-1)]
print(f"The list after the reversal is : {new_list}")
    