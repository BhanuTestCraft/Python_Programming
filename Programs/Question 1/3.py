# Add Two Number Using Lambda Function

# defining the lambda function.
addition = lambda x, y: x + y

# Taking two input from the user.
num1 = float(input("Enter the value of first number= "))
num2 = float(input("Enter the value of second number= "))

# calling the function and storing the result in a variable.
total = addition(num1, num2)

# print the final result.
print(f"Addition of two numbers {num1} and {num2} is = {total}")
