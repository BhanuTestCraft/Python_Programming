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


b1 = Bank()
b1.show_balance()
b1.deposit()
b1.show_balance()
b1.withdraw()
b1.show_balance()

# So here the limitation is no of objects that we need to create objects one by one which is not a good way and we will try to use list of objects.
