# Python program to print all odd numbers in a range.
def odd_no_range(x,y):
    odd_list = []
    for i in range(x,y+1):
        if i%2!=0:
            odd_list.append(i)
    return odd_list
start = int(input("Enter the starting number = "))
end =  int(input("Enter the ending number = "))
result = odd_no_range(start,end)
print(f"List contain only odd numbers in the given range is : {result}")
