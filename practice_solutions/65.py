"""
Ask two numbers x and y from the user. If x<y then print all the numbers from x to y, but if y<x then print all the numbers from y to x.
"""
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
if x < y:
    for i in range(x, y + 1):
        print(i, end=" ")
else:
    for i in range(y, x + 1):
        print(i, end=" ")
