# Print "Hello World" without using the print function.
# In the sys module of python we are having the object called stdout(standard output window) and through that we can print the messae in the console.

import sys

# sys.stdout.write("Hello World !!")
# sys.stdout.write("Hello World !!")
# output: Hello World !!Hello World !!
# Here in the sys module we are not having the backslash n for the new line so it will print the statements in the one line.

sys.stdout.write("Hello World !!\n")
sys.stdout.write("Hello World !!")
# output:
# Hello World !!
# Hello World !!