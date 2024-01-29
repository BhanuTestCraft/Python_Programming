def SquareIt(x):
    return x**x

assert SquareIt(2)==4,"The square of 2 should be 4"
assert SquareIt(3)==9,"The square of 3 should be 9"
# output: AssertionError: The square of 3 should be 9
# so from here we can see that there must be some incorrect code for calculating the square for the number and we can correct that code.
assert SquareIt(4)==16,"The square of 4 should be 16"

print(SquareIt(2))
print(SquareIt(3))
print(SquareIt(4))