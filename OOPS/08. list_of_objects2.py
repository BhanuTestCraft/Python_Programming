class Student:
    def __init__(self) -> None:
        self.name = input("Enter the name of student= ")
        self.age = int(input("Enter the age of student= "))

    def display_info(self):
        print(f"Name={self.name}")
        print(f"Age={self.age}")

    def change_name(self, new_name: str):
        self.name = new_name


s1 = Student()
s1.display_info()
print("-------")
s1.change_name("Akriti")
s1.display_info()
