class Student:
    def __init__(self) -> None:  # initializer
        # print("In init")
        self.name = input("Enter the name= ")
        self.age = int(input("Enter the age= "))
        self.gender = input("Enter the gender= ")
        self.roll_no = int(input("Enter the roll no= "))

    # Methods
    def info(self):
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
        print(f"Gender = {self.gender}")


s1 = Student()
s1.info()
s2 = Student()
s2.info()
# Here now problem is that by human error if we forgot to set the info for the user then there will be error.so to avoid this issue we need to initialise the variable with declaration of object itself.
# As we create the object method __init__ will run automatically.
# so to avoid the human error for set_info we can put all of that details in __init__ method.
