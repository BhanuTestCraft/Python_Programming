# Syntax:
# for var_name in sequence:
#     statements(s)
# else:
#     statements(s)

# The else block just after for/while is executed only when the loop is NOT terminated by a break statement.

# Here the else block will execute only when the for loop get executed successfully. This means loop should get completed and if we terminated it forcefully using break statement then else part will not be executed.

# In most of the programming languages (C/C++, Java, etc), the use of else statement has been restricted with the if conditional statements.


def contain_even_number(l: list):
    for element in l:
        if element % 2 == 0:
            print("Even number is present in the list")
            break
    else:
        print("Even number is not present in the list")


contain_even_number([1, 3, 5, 7, 8])
# output: Even number is present in the list (here else is not executed.)

contain_even_number([1, 3, 5, 7])
# output: Even number is not present in the list (here else statement is executed because break part is not executed in the loop.)


count = 0
while count < 1:
    count = count + 1
    print(count)
    break
else:
    print("No Break")
# Here the else staement will not get executed because while loop get terminated forcefully using break statement.
