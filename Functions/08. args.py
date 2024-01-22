# Here the challange is that we need to create function in such way that while calling that function we can put any number of argument and function will provide the result without any argument error.
def add(*args):
    # print(args)
    # Here print(args) will let us know that all the argument provided while calling the function will come as a tuple and for that we can perform the addition.
    total = 0
    for i in args:
        total += i
    print(f"sum of the numbers is = {total}")


add(1, 2, 3)
add(23, 45, 67, 89, 45, 21, 90)
add(49, 78)
