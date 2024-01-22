# Recurssion vs iteration
"""
Advantages of recurssion:
1. recurssive program are more elegant.
2. recurssive programs require few line of codes.
"""

# Factorial program using iteration and recurssion.

# method 1: iteration
num=int(input("Enter the value of number= "))
fact=1
for i in range(num,0,-1):
    fact=fact*i
print(f"Factorial of the number {num} is {fact}")

# method 2: using recurssion
num =int(input("Enter the value of the number is = "))
def fact(num):
    if num==0:
        return 1
    return num*fact(num-1)
result = fact(num)
print(f"Factorial of the number {num} is {result}")

"""
Disadvantages of recurssion:
1. recurssive programs require more space as compared to the iterative programs.
reason: as we know to track the function call we keep the track by keeping them stored in the stack, so for the process we need more function call we are occupiying the more space in the stack and that's waht we do in the recurssion by calling the same function multiple times.
2. Time complexity is also a problem when multiple recurssive calls.
--- in case of iterative method we are using for loop as the iterator for n no of times and if we plot the graph between the user input and iteration required it will be a linear graph and in the notation it is defined as O(n)
--- in case of recurssion when there is one recurssive call the the time complexity is O(n) which we can see in the factorial program but if there are two recurssive call in same function the time complexity is defined as O(2^n)
Therefor the conclusion is that when we have multiple recurssion call in the funcction then it causes the issue with the time complexity as compared to the iteration.

Therefore we use the method on the basis of our requirement:

recurssion-- when we need to write the leass amd elegant code.
iterative-- When we need to take care for the time and space complexity.
"""

"""
Advantages of iteration:
1. Iterative programs do not require stack space.
"""