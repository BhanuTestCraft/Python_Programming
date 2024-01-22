class Father:
    def __init__(self) -> None:
        self.father_name = input("Enter Father name = ")
        self._bank_balance = int(input("Enter father bank balance = "))
        self.__phone_model = input("Enter phone model = ")

    def __str__(self) -> str:  # always return the string.
        return "I am a string dunder method"

    def displayFather(self):
        print(f"Father Name = {self.father_name}")
        print(f"Father Bank Balance = {self._bank_balance}")
        print(f"Father Phone Model = {self.__phone_model}")


obj = Father()
obj.displayFather()
print("-----------")
print(obj)  # It will internally run the str method.
