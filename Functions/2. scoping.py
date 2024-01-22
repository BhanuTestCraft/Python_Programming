# def addition():
#     # Scoping of variable means the variable defined inside the function can only be used inside that function.
#     num1 = int(input("Enter the num1= "))
#     num2 = int(input("Enter the num2= "))
#     print(f"Answer = {num1+num2}")


# def subtraction():
#     num1 = int(input("Enter the num1= "))
#     num2 = int(input("Enter the num2= "))
#     print(f"Answer = {num1-num2}")


# addition()
# subtraction()
# print(num1)  # output:NameError: name 'num1' is not defined-->means it is outside the scope of the function.


def greet():
    name = input("Enter your name= ")
    print(f"your name is {name}")


name = "xyz"
greet()
print(name)
