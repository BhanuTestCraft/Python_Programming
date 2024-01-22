def circle(radius: float) -> None:
    area = 3.14 * radius * radius
    print(f"area of circle with radius {radius} = {area:.2f}")


def rectangle(length: float, breadth: float) -> None:
    area = length * breadth
    print(f"area of rectangle is = {area:.2f}")


def traingle(base: float, height: float) -> None:
    area = 0.5 * base * height
    print(f"area of triangle = {area:.2f}")


# Now the requirement is to use the same code in the other file so for that we will be going to import this file into the other file like...
# from area import *

# below condition will only print the details in console when the running file name is same as main. otherwise if we imported this in other file and then we try to run that file it will not display the below details because name of the file is different from the main file name.
if __name__ == "__main__":
    circle(20.23)
    rectangle(10, 4)
