# python program to find the power of given number using recurssion.

num = int(input("Enter the value of number: "))
pow=int(input("Enter the power value: "))
def pow_of_number(num,pow):
    if pow==0:
        return 1
    return num*pow_of_number(num,pow-1)

result= pow_of_number(2,5)
print(result)