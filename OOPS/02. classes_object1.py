# First letter of the class should be written in caps not compulsary but widely used.
class Student:
    # variables created inside the class are called as
    # Class variables/Attributes.
    roll_no = 0
    name = ""
    age = 0
    gender = ""

    # Methods
    def info(self):
        # self must be written as parameter if it is written within the class because it will indicate that function belongs to the created class.
        print(f"Name = {self.name}")
        # To acces the attribute of class inside the function we need to use self keyword.
        print(f"Age = {self.age}")
        print(f"Gender = {self.gender}")

    def set_info(self):
        self.name = input("Enter the name= ")
        self.age = int(input("Enter the age= "))
        self.gender = input("Enter the gender= ")
        self.roll_no = int(input("Enter the roll no= "))


s1 = Student()
# Created one object s1 which will hold the information of student 1.
s2 = Student()
s1.roll_no = 2
# s1.name = "Bhanu"
# s1.gender = "male"
# s1.age = 27
s1.set_info()
s2.set_info()
print("----------")
s1.info()
s2.info()


# print(s1.roll_no)
# print(s1.name)

# print("-----------")
# print(s2.roll_no)
# print(s2.name)
