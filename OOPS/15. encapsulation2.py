# Public, private, Protected
from random import randint


# To make any variable as protected inside the class we can use double underscore before the variable.
class Bank:
    def __init__(self) -> None:
        self.name = input("Enter name = ")
        self.__account_no = randint(100000, 999999)
        self.__balance = 0

    def display(self):
        print(f"Account Number = {self.__account_no}")
        print(f"Name = {self.name}")
        print(f"balance = {self.__balance}")


obj = Bank()
obj.display()
print(obj.__account_no)
# It will through the error : AttributeError: 'Bank' object has no attribute '__account_no'
# obj.__account_no = 1
# since now we have made the account_no variable as protected which means now it will not be able to access the variable and do the changes.
obj.display()
