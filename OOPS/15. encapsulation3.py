from random import randint


# To make any variable as protected inside the class we can use double underscore before the variable.
class Bank:
    def __init__(self) -> None:
        self.name = input("Enter name = ")
        self.__account_no = randint(100000, 999999)
        self.__balance = 0

    # Let us assume we only need to display the balance then we will use getter.
    def displayBalance(self):  # getter
        print(self.__balance)

    def setBalance(self, newAmount):  # setter
        self.__balance = newAmount

    def display(self):
        print(f"Account Number = {self.__account_no}")
        print(f"Name = {self.name}")
        print(f"balance = {self.__balance}")


obj = Bank()
obj.display()
print("-----------")
# obj.setBalance(1000)
# obj.displayBalance()

# Never do this.
print(obj._Bank__balance)
# Syntax: obj._className__variableName
# Even after having balance as a private variable we can access outside the class as in python it is not followed strictly.
