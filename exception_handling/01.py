# syntax error vs run time error

# 1. syntax error: These error occurs when we are not following the rule set required to write any program and as we run the program we will get the error named as syntax error.(Basically we can say these are the human errors and can be only corrected by programmer to get the desired result.)
# x=10
# if x==10
#    print(f"value of x is {x}")
# output: SyntaxError: expected ':'
x=10
if x==10:
   print(f"value of x is {x}")
# output: value of x is 10
   
#  2. runtime error: These error occured when we have written some incorrect logic or user have entered incorrect inputs or due to any memory issue and during the run time we will be getting the error and these errors are known as the "EXCEPTIONS".
x=int(input("Enter the first number = "))
y=int(input("Enter the second number = "))
print(f"The divison of two numbers is {x/y}")
# output: ZeroDivisionError: division by zero
# Here we have taken denominator as 0 and that is causing run time error or we can say that it's an exception it is giving with the specific set of the inputs.
# some times we can get the valueerror that is very common.

f = open("xyzxyz.txt")
print(f.read())
# FileNotFoundError: [Errno 2] No such file or directory: 'xyzxyz.txt'
# Here we are not having any error in our program but during run time we got to know that there is no such file existing at the root directory we are pointing and that is why it is giving "FileNotFoundError" during the run time which is also an exception.

"""
objective of Exception handling:
The objective of the exception handling is the graceful/normal termination of your application or program.(i.e we should not block our resource and not miss anything important.)

Exception handling does not mean to repair any exception. we have to define the alternative way to continue rest of program normally.This way of defining alternative is nothing the exception handling.

try:
   read data from the remote file locating at london
except FileNotFoundError:
    use the local file and continue the rest of program normally
"""