# adding numbers using function.


# Declaring the function with name addition.
def addition(x: float, y: float) -> float:
    return x + y


# Taking two input from the user.
num1 = float(input("Enter the value of first number= "))
num2 = float(input("Enter the value of second number= "))

# calling the function and storing the result in variable as function is returning something.
total = addition(num1, num2)

# Print the final result.
print(f"Addition of numbers {num1} and {num2} is = {total}")
