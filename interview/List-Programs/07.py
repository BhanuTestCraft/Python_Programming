# Python program to find sum of elements in list.
my_list=[1,2,3,4,5]

# Method 1:
def sumOfElements(my_list):
    sum=0
    for value in my_list:
        sum+=value
    return sum
result = sumOfElements(my_list)
print(f"Sum of the element present in the list is : {result}")

# Method 2:
my_list=[1,2,3,4,5]
def sumOfElements(my_list):
    index=0
    sum=0
    while index < len(my_list):
        sum+=my_list[index]
        index+=1
    return sum
result = sumOfElements(my_list)
print(f"Sum of the element present in the list is : {result}")
