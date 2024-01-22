"""
Python Program for n-th Fibonacci number
"""


def nth_fibonacci(n: int) -> int:
    fib = [0, 1]

    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])

    print(f"The entire fibonacci series is = {fib}")
    return fib[n]


# Input from the user
n = int(input("Enter the value of n: "))

# Calculate and print the nth Fibonacci number
result = nth_fibonacci(n)
print(f"The {n}-th Fibonacci number is: {result}")
