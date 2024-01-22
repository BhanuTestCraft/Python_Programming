"""
Ask a number from user. Print the multiplication table of that number.
Example
"""
num = int(input("Enter the number: "))
count = 1
while count <= 10:
    product = num * count
    print(f"{num}*{count}={product}")
    count += 1
