def addition(num1, num2=0):
    # Here we have initialised the default value for num2=0, which means if while calling the function we are noot sending the argument for num2 it will take the default valu as 0.
    total = num1 + num2
    print(total)


addition(100)
# Here num1=100 and num2=0 because we have not sended any argument for the num2 so it has picked the default value.

addition(100, 200)
# Here we are passing both the argument values i.e for num1 and num2 so num1=100 and num2=200.
