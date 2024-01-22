"""
Python Program to Find Area of a Circle
"""


def area(x: float) -> float:
    pi = 3.14
    return pi * x * x


radius = float(input("Enter the value of radius = "))
result = area(radius)
print(f"The area of circle is {result:.2f}")
