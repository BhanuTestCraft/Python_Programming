# Python Program for n-th Fibonacci number.
def Fibonacci(n):
    if n<0:
        print("Incorrect input")
    elif n==1:
        return 1
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

print(Fibonacci(10))

def fibonacci(num):
    a = 0
    b = 1
    if num < 0:
        print("Incorrect input")
    elif num == 0:
        return a
    elif num == 1:
        return b
    else:
        for i in range(2, num+1):
            c = a + b
            a = b
            b = c
        return b
 
print(fibonacci(10))