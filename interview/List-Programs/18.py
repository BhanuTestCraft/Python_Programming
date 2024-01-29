# Python program to print all positive numbers in a range.

def positive_no_range(x,y):
    for value in range (x,y+1):
        if value>=0:
            print(value,end=" ")
start= int(input("Enter the starting number = "))
end = int(input("Enter the ending number = "))
positive_no_range(start,end)