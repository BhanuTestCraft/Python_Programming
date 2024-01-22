# encapsulation: meand data hiding.
# Data hiding is done through access modifiers.
from random import randint

# Here inside the class there are four things in which three are the variables and one is a method which is accessible outside the class which means they are public by default.


class Bank:
    def __init__(self) -> None:
        self.name = input("Enter name = ")
        self.account_no = randint(100000, 999999)
        self.balance = 0

    def display(self):
        print(f"Account Number = {self.account_no}")
        print(f"Name = {self.name}")
        print(f"balance = {self.balance}")


obj = Bank()
obj.display()
obj.account_no = 1
# Here we are able to change the account number through the object which is not correct way as it can lead to data breach.
# So here we will do something so that that class variable will not be accessed outside the class.
obj.display()
