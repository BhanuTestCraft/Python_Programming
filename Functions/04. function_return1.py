# Function with the return statement.
def addition(num1, num2):
    total = num1 + num2
    return total


# addition(10,20) It will not give any output in the console because if any function is returning some value then it need to be stored in some variable.
#  we can also use print in place of return inside the function but most of the times when we see the codes for any function it do return something.

sum = addition(10, 20)
print(f"sum of two numbers is= {sum}")


# function with print staement.
def addition(num1, num2):
    total = num1 + num2
    print(total)


x = addition(10, 20)
# Here we will not get any return value so nothing will get stored in the x and print statement will print the value as none.
print(x)
