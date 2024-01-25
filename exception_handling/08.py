# Default except block
"""
1. We can use default except block to handle any kind of the exception.
2. In default except block, genearlly we can print  exception information to the console.
3. If default except block is defined then compulsary it must be the last except block otherwise we will get the syntax error.
"""

try:
    x=int(input("Enter the value of x: "))
    y=int(input("Enter the value of y: "))
    print(x/y)
except ZeroDivisionError as message:
    print("ZeroDivisionError : cannot divide with zero")
except:
    print("Default except: Please provide the valid inputs only")

# output 1:
# Enter the value of x: 10
# Enter the value of y: 0
# ZeroDivisionError : cannot divide with zero
    
# output 2:
# Enter the value of x: 10
# Enter the value of y: two
# Default except: Please provide the valid inputs only 
    
