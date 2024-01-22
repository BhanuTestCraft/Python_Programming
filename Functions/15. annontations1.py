# without annotations
# def add(x, y):
#     total = x + y
#     print(total)
# add(10, 20)
# Here when we hover on the add function it will display as -->None which means it is nit returning anything.


# with annotations
def add(x: int, y: int) -> int:
    # Still it will not strict us in passing the argument while calling the function.It is just used to display while hovering on function for user to know what kind of data input can be entered.
    total = x + y
    return total


c = add(10, 20)
# Here if we will hover on the add function then we will see --->int which means this function is returning something.
print(c)


def greet(name: str, age: int, percentage: float) -> None:
    print(f"name is {name}")
    print(f"age is {age}")
    print(f"percentage is {percentage}")


greet("Bhanu", 27, 86)
# Here if we will hover over the function greet we will be able to see what set of parameter and there data type is needed and also what function is returning to us.
