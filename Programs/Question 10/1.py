"""
Program to print ASCII Value of a character
"""


def ascii_value(x: str) -> int:
    return ord(x)


chr = input("Enter the value of any character= ")
result = ascii_value(chr)
print(f"ASCII value of charcter {chr} is {result}")
