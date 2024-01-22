# Protected: means base class can access i.e father class and also the derived child class can also access the same.

# syntax: to make any variable as protected we can use single underscore before the variable.


class Father:
    def __init__(self) -> None:
        self.father_name = input("Enter Father name = ")  # public
        self._bank_balance = int(input("Enter father bank balance = "))  # protected
        self.__phone_model = input("Enter phone model = ")  # private

    def displayFather(self):
        print(f"Father Name = {self.father_name}")
        print(f"Father Bank Balance = {self._bank_balance}")
        print(f"Father Phone Model = {self.__phone_model}")


class Child(Father):
    def __init__(self) -> None:
        super().__init__()
        self.child_name = input("Enter child name = ")

    def displayChildInfo(self):
        print(f"Child Name = {self.child_name}")
        print(f"My father has {self._bank_balance} amount in bank.")


ch = Child()
ch.displayChildInfo()
