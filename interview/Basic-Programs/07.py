# Python Program for Sum of squares of first n natural numbers.
def square(n):
    total = 0
    for i in range(1,n+1):
        total+=i*i
    return total

n = int(input("Enter the number = "))
result = square(n)
print(f"sum of first {n} natural numbers is {result}")
