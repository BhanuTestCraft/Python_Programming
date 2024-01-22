import pickle


class Student:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


s = Student("Anirudh", 18)
f = open("name.txt", "wb")
# we use "w" mode only for text and here we are working with some object and memory so we need to open it in binary mode.
pickle.dump(s, f)
f.close()


# WRITE
# x = "Code and Debug"
# with open("name.txt", "w") as f:
#     f.write(str(s))

# READ
# with open("name.txt", "r") as f:
#     s = f.read()
#     print(s)
#     print(type(s))
