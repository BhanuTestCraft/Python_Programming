# write a python program to check the number is prome or not using the recurssive way.
num=int(input("Enter the value of number: "))
def is_prime(num,i):
    if i==1:
        return 1
    if num%i==0:
        return 0
    return is_prime(num,i-1)

ind= is_prime(num,num-1)

if ind==1:
    print("Number is prime number")

if ind==0:
    print("Number is not a prime number")