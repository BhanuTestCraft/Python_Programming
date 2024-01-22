class Father:
    def __init__(self) -> None:
        self.father_name = input("Enter Father name = ")
        self._bank_balance = int(input("Enter father bank balance = "))
        self.__phone_model = input("Enter phone model = ")

    def __str__(self) -> str:  # always return the string.
        return f"Father Name = {self.father_name}\nFather Bank Balance = {self._bank_balance}\nFather Phone Model = {self.__phone_model}"


obj1 = Father()
obj2 = Father()
print("-----------")
print(obj1)  # It will internally run the str method.
print(obj2)
