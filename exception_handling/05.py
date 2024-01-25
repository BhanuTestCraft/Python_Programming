# How to print the exception information.

try:
    print(10/0)
except ZeroDivisionError as message:
    print(f"type of the exception is : {type(message)}")
# output: type of the exception is : <class 'ZeroDivisionError'>
    
try:
    print(10/0)
except ZeroDivisionError as message:
    print(f"type of the exception is : {message.__class__}")
# output: type of the exception is : <class 'ZeroDivisionError'>
    
try:
    print(10/0)
except ZeroDivisionError as message:
    print(f"exception class name is : {message.__class__.__name__}")
# output: exception class name is : ZeroDivisionError
    
try:
    print(10/0)
except ZeroDivisionError as message:
    print(f"description of the exception is : {message}")
# output: description of the exception is : division by zero
    
try:
    x=int(input("Enter the value of x= "))
    y=int(input("Enter the value of y= "))
    print(x/y)
except BaseException as message:
    print(f"type of the exception is : {type(message)}")
    print(f"type of the exception is : {message.__class__}")
    print(f"name of the exception is : {message.__class__.__name__}")
    print(f"description of the exception is : {message}")
# output 1:
# Enter the value of x= 10
# Enter the value of y= 0
# type of the exception is : <class 'ZeroDivisionError'>
# type of the exception is : <class 'ZeroDivisionError'>
# name of the exception is : ZeroDivisionError
# description of the exception is : division by zero
    
# output 2:
# Enter the value of x= 10
# Enter the value of y= two
# type of the exception is : <class 'ValueError'>
# type of the exception is : <class 'ValueError'>
# name of the exception is : ValueError
# description of the exception is : invalid literal for int() with base 10: 'two'