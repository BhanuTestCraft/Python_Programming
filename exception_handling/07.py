# single except block that can handle multiple different exceptions.
# If the handling code for the different exception is the same for different exception we can use on except block in place of the multiple except blocks.
# syntax: except(ZeroDivisionError,ValueError,NameError) as message:

try:
    x=int(input("Enter the value of x: "))
    y=int(input("Enter the value of y: "))
    print(x/y)
except (ZeroDivisionError,ValueError) as message:
    print(f"Raised exception name is : {message.__class__.__name__}")
    print("Please provide the valid input only !!")

# output 1:
# Enter the value of x: 10
# Enter the value of y: 0
# Raised exception name is : ZeroDivisionError
# Please provide the valid input only !!
    
# output 2:
# Enter the value of x: 10
# Enter the value of y: two
# Raised exception name is : ValueError
# Please provide the valid input only !!