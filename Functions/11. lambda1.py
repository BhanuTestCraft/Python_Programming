# Lambda Function---> Anonymous Function.

# def add_numbers(n1, n2, n3):
#     return n1 + n2 + n3
# Here in this function we are not doing much i.e only returning something so we can do it more concisely with lambda function.

# Since lambda function are anonymous,we are not having any name for that function while defination, so in this case we need to store it in a variable.
add_numbers = lambda n1, n2, n3: n1 + n2 + n3
result = add_numbers(10, 20, 30)
print(result)
