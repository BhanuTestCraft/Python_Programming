"""
Whenever a runtime error occurs, it creates an exception. Usually, the program
stops and Python prints an error message.
For example, dividing by zero creates an exception:
>>> print 55/0
ZeroDivisionError: integer division or modulo
So does accessing a nonexistent list item:
>>> a = []
>>> print a[5]
IndexError: list index out of range
Or accessing a key that isn’t in the dictionary:
>>> b = {}
>>> print b[’what’]
KeyError: what
Or trying to open a nonexistent file:
>>> f = open("Idontexist", "r")
IOError: [Errno 2] No such file or directory: ’Idontexist’
In each case, the error message has two parts: the type of error before the colon,
and specifics about the error after the colon. Normally Python also prints a
traceback of where the program was, but we have omitted that from the examples.

Sometimes we want to execute an operation that could cause an exception, but
we don’t want the program to stop. We can handle the exception using the try
and except statements.
For example, we might prompt the user for the name of a file and then try to
open it. If the file doesn’t exist, we don’t want the program to crash; we want to
handle the exception:
"""


def exists(filename):
    try:
        f = open(filename, "r")
        f.close()
        print(True)
    except IOError as e:
        print(False)
        print(f"Error: {e}")


exists("/Users/bhanu/Personal/Python_Coding/file_operations/picc.txt")
