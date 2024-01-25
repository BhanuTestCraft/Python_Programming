# Finally block.
"""
1. It is not recommended to place clean up code(resource deallocation code like closing database connection etc) inside the try block, because there is no gaurantee for execution of every statement inside the try block.
2. It is not recommended to keep cleanup code inside the except block, because if there is no exception then except block won't get executed.
3. Hence we require some place to maintain cleanup code which is executed always irrespective of whether exception handled or not handled. suh=ch type of best place is nothing but finally block.

syntax: 
try: 
   risky code
except: 
     Handling code
finally:
       clean up code
"""

# case 1: There is no exception
try:
    print("try")
except:
    print("except")
finally:
    print("finally")
# output:
# try
# finally
    
# case 2: exception handled 
try:
    print("try")
    print(10/0)
except ZeroDivisionError as message:
    print(f"type: {type(message)}")
finally:
    print(f"finally")
# output:
# try
# type: <class 'ZeroDivisionError'>
# finally
    
# case 3: exception raised but not handled
try:
    print("try")
    print(10/0)
finally:
    print("finally")
# output:
# try
# finally
# ZeroDivisionError: division by zero