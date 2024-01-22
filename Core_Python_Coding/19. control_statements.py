"""
control statements are an essential aspect of any programming language,including python. control statements in python are used to manage the flow of execution of a program based on certain condition.

eg:---> we know that for loop will not stop till it get completed but if we want to stop that with particular condition then it is a control statement for the loop

1. break: to stop a loop.(It is used when we don't know when the condition will get satisfied so we will put the break statement within certain condition to stop the loop or we can say program will come outside the loop.)

2. Continue: In case of continue it will not execute the line of codes written after the continue statement within the loop and loop will move forward for the next iteration.

3. Pass: In this case when we are not sure of the code under any condition then we use pass statement in that case so that it will not through any error and it will not disturb anything in the program.
"""

# for i in range(1,101):
#     print(i,end=" ")
#     if i==10:
#         break

# for i in range(1,11):
#     if i==5:
#         continue
#     print(i)
#     print("Done")
#     print("Bye")
# print("Program Finish")

for i in range(1,11):
    if i==5:
        pass
    print(i)
    print("Done")
    print("Bye")
print("Program Finish")