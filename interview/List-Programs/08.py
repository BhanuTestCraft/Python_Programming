# Python | Multiply all numbers in the list.
my_list = [1,2,3,4,5]

def multiply_elements(my_list):
    product=1
    for value in my_list:
        product*=value
    return product

result = multiply_elements(my_list)
print(f"multiplication of all the elements in the given list is : {result}")

def multiply_elements(my_list):
    product=1
    index = 0
    while index<len(my_list):
        product*=my_list[index]
        index+=1
    return product
result = multiply_elements(my_list)
print(f"multiplication of all the elements in the given list is : {result}")