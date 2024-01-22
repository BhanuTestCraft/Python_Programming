# declaring lambda function.
largest = lambda x, y: x if x > y else y

# Taking two input from the user.
num1 = int(input("Enter the value of first number = "))
num2 = int(input("Enter the value of second number = "))

# print the final result.
print(f"{largest(num1,num2)} is a maximum number")
