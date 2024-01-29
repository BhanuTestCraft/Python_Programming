# Python program to print all even numbers in a range.
def even_no_range(x,y):
    new_list = []
    for i in range(x,y+1):
        if i%2==0:
            new_list.append(i)
    return new_list
start = int(input("Enter the starting number = "))
end   = int(input("Enter the ending number = "))
result = even_no_range(start,end)
print(f"The even numbers between start and end are given in list is : {result}")
