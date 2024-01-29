"""
Assertions: The main purpose of the assertion is used for debugging.

Debugging: The process of identifying and fixing the bug is known as the debugging.

most commonly used way to perform debugging is that the use of the print statements. Because with print statement we can see that if it is printing some line that gives us the surity that code above that line is working fine.

we can say that let us assume we are having large code base then to put validation where we can do we put the debug point as the assertion statement so that we will know the issue immediately where we are not getting expected output and will help us to get the final output as the expected one.

But using the print statement for the debugging have one issue is that we need to remove the print statements used just for debugging after everything is working fine as they are not the part of required code. otherwise that print statements get executed and printed everytime on the console/logs which is just the waste of resources.

To avoid such situation in debugging we do use the assertions.

Types of assert statements:
1. Simple Version
2. very simple version(Augmented version)

-----------------------------------
1. simple version:
assert condtional_expression
--> it will check the conditional expression and if that is true then it confirms that till this part of the code is correct and it will exceute the further code.
--> If the expression return the false it will stop execution by raising the AssertionError.

2. Augmented version:
assert condtional_expression, "message"
--> Whenever this condition return the value as false it will print the additional message on the console provided in the assert statement.
"""
x=20
assert x==20
print(f"value of x is : {x}")


# x=10
# assert x>10, "The value for x is not greater than 10"
# print(f"value of x is : {x}")

"""
def SquareIt(x):
    return x**x

assert SquareIt(2)==4,"The square of 2 should be 4"
assert SquareIt(3)==9,"The square of 3 should be 9"
# output: AssertionError: The square of 3 should be 9
# so from here we can see that there must be some incorrect code for calculating the square for the number and we can correct that code.
assert SquareIt(4)==16,"The square of 4 should be 16"

print(SquareIt(2))
print(SquareIt(3))
print(SquareIt(4))"""

def SquareIt(x):
    return x*x

assert SquareIt(2)==4,"The square of 2 should be 4"
assert SquareIt(3)==9,"The square of 3 should be 9"
assert SquareIt(4)==16,"The square of 4 should be 16"

print(SquareIt(2))
print(SquareIt(3))
print(SquareIt(4))