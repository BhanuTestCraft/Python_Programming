# Python | Program to print duplicates from a list of integers.
my_list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

def duplicate_list(list):
    new_list = []
    for value in list:
        n=list.count(value)
        if n>1:
            if new_list.count(value)==0:
                new_list.append(value)
    return new_list
result = duplicate_list(my_list)
print(f"The list having only duplicate elements is : {result}")

element_count = {}
duplicate_list =[]
for value in my_list:
    if value in element_count:
        element_count[value]+=1
    else:
        element_count[value]=1
for value,count in element_count.items():
    if count>1:
        duplicate_list.append(value)
print(duplicate_list)
