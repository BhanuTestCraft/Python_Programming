# Python Program to Check Prime Number.
def is_prime(num):
    factors=0
    for i in range(1,num+1):
        if num%i==0:
            factors+=1
    if factors ==2:
        return True
    else:
        return False
num = int(input("Enter a number: "))
result = is_prime(num)
print(f"{num} is prime: {result}")