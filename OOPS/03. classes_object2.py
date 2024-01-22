class Student:
    # Methods
    def info(self):
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
        print(f"Gender = {self.gender}")

    def set_info(self):
        self.name = input("Enter the name= ")
        # basically this is creating a new variable name only. so it is not neccessary to created default variable in the class.
        self.age = int(input("Enter the age= "))
        self.gender = input("Enter the gender= ")
        self.roll_no = int(input("Enter the roll no= "))


s1 = Student()
s1.set_info()
# Here now problem is that by human error if we forgot to set the info for the user then there will be error.so to avoid this issue we need to initialise the variable with declaration of object itself.
s1.info()
# If we execute s1.info function before set_info then we have not created the variable with name,age and gender so it will give us an error.
