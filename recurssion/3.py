# write python program to find factorial of the number.
# 5!= 5*4*3*2*1
#  5!= 5*4! = 5*4*3! = 5*4*3*2! = 5*4*3*2! = 5*4*3*2*1! = 5*4*3*2*1*0! = 5*4*3*2*1*1

num = int(input("Enter the value of num: "))
def fact(num):
    if num==0:
        return 1
    return num*fact(num-1)

if num<0:
    print("Factorial of negative number is not defined.")
elif num==0:
    print("Factorial of 0 is 1")
else:
    result= fact(num)
    print(f"Factorial of {num} is {result}")

