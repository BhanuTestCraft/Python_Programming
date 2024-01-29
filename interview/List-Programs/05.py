# Different ways to clear a list in Python.
my_list=[1,2,3,4,5]

# Method 1: using the clear function
print(f"List before clearing is : {my_list}")
result= my_list.clear()
print(f"List after clearing is : {my_list}")

# Method 2: using the del method
my_list=[1,2,3,4,5]
def clearList(my_list):
    print(f"List before clearing is: {my_list}")
    del my_list[:]
    return my_list
result = clearList(my_list)
print(f"The list after clearing is: {result}")

# Method 3: using pop method
my_list=[1,2,3,4,5]
def clearList(my_list):
    print(f"List before clearing is : {my_list}")
    while len(my_list)!=0:
        my_list.pop()
    return my_list

result=clearList(my_list)
print(f"List after clearing is : {result}")