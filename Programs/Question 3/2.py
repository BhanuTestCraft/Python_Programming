# declaring the function
def factorial(n: int) -> int:
    if n < 0:
        return 0
    elif n == 0 and n == 1:
        return 1
    else:
        result = 1
        while n > 1:
            result *= n
            n -= 1
        return result


# taking any input from the user.
num = int(input("Enter the value of number= "))

# calling the function
output = factorial(num)

# print the final output
print(f"factorial of number {num} is {output}")
