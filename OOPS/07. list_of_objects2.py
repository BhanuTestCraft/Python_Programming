from random import randint


class Bank:
    def __init__(self) -> None:
        self.account = randint(100000, 999999)
        self.full_name = input("Enter the name= ")
        self.balance = 0
        self.phone_number = int(input("Enter phone number= "))

    def show_info(self) -> None:
        print(f"Account number= {self.account}")
        print(f"full name= {self.full_name}")
        print(f"balance= {self.balance}")
        print(f"phone number= {self.phone_number}\n")

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


def check_account_exist(acc_no: int):
    global banks
    for obj in banks:
        if obj.account == acc_no:
            return obj
    return None


while True:
    print("1. Create account")
    print("2. show all bank details")
    print("3. Deposit amount")
    print("4. Withdraw amount")
    print("5. Transfer amount")
    print("6. exit")
    choice = int(input("Enter your choice= "))
    if choice == 1:
        obj = Bank()
        banks.append(obj)
        print(banks)
    elif choice == 2:
        if len(banks) == 0:
            print("No accounts have been created yet")
        else:
            for account in banks:
                account.show_info()
    elif choice == 3:
        if len(banks) == 0:
            print("No account have been created")
        else:
            acc_no = int(input("Enter the account number to deposit= "))
            for obj in banks:
                if obj.account == acc_no:
                    obj.deposit()
                    break

    elif choice == 4:
        if len(banks) == 0:
            print("No account have been created")
        else:
            acc_no = int(input("Enter the account number to withdraw from= "))
            for obj in banks:
                if obj.account == acc_no:
                    obj.withdraw()
                    break

    elif choice == 5:
        from_acc_no = int(
            input("Enter the account number from which you want to transfer= ")
        )
        to_acc_no = int(
            input("Enter the account number to which we need to transfer= ")
        )
        from_acc_obj = check_account_exist(from_acc_no)
        to_acc_obj = check_account_exist(to_acc_no)
        if from_acc_obj != None and to_acc_obj != None:
            transfer_amount = int(input("Enter the transfer amount= "))
            if from_acc_obj.balance < transfer_amount:
                print("Insufficient balance")
            else:
                from_acc_obj.balance -= transfer_amount
                to_acc_obj.balance += transfer_amount
        else:
            print("Account does not exist")

    elif choice == 6:
        break
    else:
        print("Invalid choice")
