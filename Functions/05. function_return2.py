"""
Ask two numbers from the user.
calculate sum of the numbers.
print if the sum is odd or even.

need to create two functions.
add() and check()
"""


def add(n1, n2):
    total = n1 + n2
    return total


def check(num):
    # There is no way to send the value of total to num until the add function is not returning something and that's why it is important to use the return statement.
    if num % 2 == 0:
        # print(f"sum is Even")
        return "EVEN"
    else:
        # print(f"sum is Odd")
        return "ODD"


x = int(input("Enter the value of first number= "))
y = int(input("Enter the value of second number= "))
s = add(x, y)
print(f"sum of the numbers is {s}")
# check(s)
c = check(s)
print(c)
