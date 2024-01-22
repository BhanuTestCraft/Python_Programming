class Car:
    def __init__(self) -> None:
        print("CAR INIT")

    def set_info(self):
        self.color = input("Enter car color = ")
        self.type = input("Enter type = ")
        self.mileage = float(input("Enter mileage = "))
        self.seat_capacity = int(input("Enter seat capacity = "))

    def base_info(self):
        print(f"color = {self.color}")
        print(f"type = {self.type}")
        print(f"mileage = {self.mileage}")
        print(f"seat_capacity = {self.seat_capacity}")


class Audi(Car):
    def __init__(self) -> None:
        print("AUDI INIT")

    def set_audi_info(self):
        self.set_info()
        self.electric = input("Enter electric = ")
        self.city = input("Enter city = ")

    def audi_info(self):
        print(f"Electric = {self.electric}")
        print(f"City = {self.city}")

    def show_full_info(self):
        self.base_info()
        self.audi_info()


c1 = Audi()
# Here if we run the program it will only run the init for the derived class not for the parent class.
c1.set_audi_info()
# c1.base_info()
# c1.audi_info()
print("----------")
c1.show_full_info()
