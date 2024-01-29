# Check if element exists in list in Python.
my_list=[1,2,3,4,5]
num = int(input("Enter any number = "))

# Method 1:
# def elementExist(num,my_list):
#     if num in my_list:
#         print(f"The number {num} do exist in the given list")
#     else:
#         print(f"The number {num} do not exist in the given list")

# print(elementExist(num,my_list))

# Method 2:
def elementExist(num,my_list):
    for value in my_list:
        if value==num:
            print(f"The given number {num} do exist in the list")
            break
    else:
        print(f"The given number {num} do not exist in the list")
        
print(elementExist(num,my_list))

# Method 3
def elementExist(num,my_list):
    counter_value = my_list.count(num)
    if counter_value>0:
        print(f"The given number {num} do exist in the list")
        return True
    else:
        print(f"The given number {num} does not exist in the list")
        return False
result = elementExist(num,my_list)
