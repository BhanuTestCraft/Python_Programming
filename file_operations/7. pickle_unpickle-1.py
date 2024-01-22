class Student:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


# s = Student("Bhanu", 27)


# File handling for text files
# write
# x = "Code and Debug"
# In write mode if file does exist it will overide all the text present in the file with our input and if file is not existing it will create the file and write the text.
# with open("name.txt", "w") as f:
#     f.write(str(s))
# Here we are writing the object into the text file.

# Read
with open("name.txt", "r") as f:
    s = f.read()
    print(s, type(s))
# output: <__main__.Student object at 0x1022f8b50> <class 'str'>

# Problem: So here the problem statement is we can write the strings easily and can read that from the file but in case of object it is not reading the object details. so we need the solution for writing and reading the objects.
