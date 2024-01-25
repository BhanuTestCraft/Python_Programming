# try with multiple except block
"""
1. The way of handling the exception do varies from the exception to exception.
2. Hence for every possible exception type, we have to take a separate except block.try with multiple except block is possible and is recommended.
3. If we are using try with multiple except block then the order of these except blocks are important as python virtual machine will always consider from top to bottom until matched except block is identified.
"""

try:
    x=int(input("Enter the value of x = "))
    y=int(input("Enter the value of y = "))
    print(x/y)
except ZeroDivisionError as message:
    print(f"The tpye of error is : {type(message)}")
    print(f"The description for the error is : {message}")
except ValueError as message:
    print(f"The tpye of error is : {type(message)}")
    print(f"The description for the error is : {message}")
    

# output 1:
# Enter the value of x = 10
# Enter the value of y = 0
# The tpye of error is : <class 'ZeroDivisionError'> 
# The description for the error is : division by zero
    
# output 2:
# Enter the value of x = 10
# Enter the value of y = two
# The tpye of error is : <class 'ValueError'>
# The description for the error is : invalid literal for int() with base 10: 'two'   
    

try:
    print(10/0)
except ZeroDivisionError as message:
    print(f"ZeroDivisionError : {message}")
except ArithmeticError as message:
    print(f"AritmeticError : {message}")
# output: ZeroDivisionError : division by zero
    
try:
    print(10/0)
except ArithmeticError as message:
    print(f"AritmeticError : {message}")
except ZeroDivisionError as message:
    print(f"ZeroDivisionError : {message}")
# output: AritmeticError : division by zero
# since ZeroDivisionError is the base class of the ArithmeticError so ArithmeticError as except block can handle the exception if it is placed above in the order while writing the code.