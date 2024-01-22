"""
Ask N from user. N means number of lines. Then print the following pattern.
enter n=3
3 3 3 3 3
2 2 2 2 2
1 1 1 1 1
"""
n = int(input("Enter the value of n= "))
for i in range(n, 0, -1):
    for j in range(1, 6):
        print(i, end=" ")
    print()
