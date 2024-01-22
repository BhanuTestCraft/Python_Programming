# If your program detects an error condition, you can make it raise an exception.
# Here is an example that gets input from the user and checks for the value 17.
# Assuming that 17 is not valid input for some reason, we raise an exception.


def inputNumber():
    x = input("Pick a number: ")
    if x == 17:
        raise ValueError("17 is a bad number")
    return x
