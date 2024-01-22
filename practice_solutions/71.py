"""
Ask N from user. N means number of lines. Then print the following pattern.
enter n=3
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
"""
n = int(input("Enter the value of n= "))
for i in range(1, n + 1):
    for j in range(1, 6):
        print(i, end=" ")
    print()
