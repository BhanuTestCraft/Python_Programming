"""
Ask a number from user. Print the multiplication table of that number.
Example
Enter a number = 8
8 x 1 = 8
8 x 2 = 16
8 x 3 = 24
"""
num = int(input("Enter the number: "))
for i in range(1, 11):
    result = num * i
    print(f"{num}*{i}={result}")
    i += 1
