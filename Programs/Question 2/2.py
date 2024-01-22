# creating one function for finding the largest of two numbers
def largest(a: int, b: int) -> None:
    if a > b:
        print(f"{a} is the largest number from {a} and {b}")
    elif b > a:
        print(f"{b} is the largest number from {a} and {b}")
    else:
        print("User input numbers are equal in value")


# Taking two numbers from the user.
num1 = int(input("Enter the value of first number= "))
num2 = int(input("Enter the value of second number= "))

# calling the function
largest(num1, num2)
