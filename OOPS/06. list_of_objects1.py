from random import randint


class Bank:
    def __init__(self) -> None:
        self.account = randint(100000, 999999)
        self.full_name = input("Enter the name= ")
        self.balance = 0
        self.phone_number = int(input("Enter phone number= "))

    def show_balance(self) -> None:
        print(f"current balance = {self.balance}")

    def withdraw(self) -> None:
        amount = int(input("Enter the amount to withdraw= "))
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount

    def deposit(self) -> None:
        amount = int(input("Enter the amount to deposit= "))
        self.balance += amount


banks = []
x = Bank()
banks.append(x)
print(banks)

y = Bank()
banks.append(y)
print(banks)

banks[0].show_balance()
banks[1].deposit()
banks[1].show_balance()
