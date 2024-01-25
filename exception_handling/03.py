# Customized exception handling using the try except block.
"""
without try except block
print("Hello")  --> assume this as opening db connection
print(10/0)     --> assume this as reading from db and some error occur.
print("Bye")    --> assume this as closing db connection.

output:
Hello
ZeroDivisonError
"""
# Since db connection will not be closed and that will cause the resource wastage and that is not recommended.
# This is the abnormal termination of our program.

# The part of code we know that can cause or raise the exception is known as the risky code and that should be written inside the try block, and to handle that risky code we need to write some sort of code in the except block.
"""
try:
   risky code.
except:
      code to handle the risky code.
"""

"""
with try-except block:
print("Hello")  #this code is not risky so outside try-except.
try:
   print(10/0)
except ZeroDivisi onError:
      print(10/2)
print("Bye")

This format of coding will help us in graceful or the normal termination of the program.

output:
Hello
5.0
Bye
"""