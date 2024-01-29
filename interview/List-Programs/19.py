# Python program to print all negative numbers in a range.
def negative_no_range(x,y):
    for value in range(x,y+1):
        if value<0:
            print(value,end=" ")
start = int(input("Enter the starting number = "))
end = int(input("Enter the ending number = "))
negative_no_range(start,end)        