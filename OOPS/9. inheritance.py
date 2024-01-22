"""
Inheritance means inheriting something from base class.
car prop: color, type, mileage, seat capacity
audi: color, type, mileage, seat capacity, branch, city
maruti: color, type, mileage, seat capacity, ....
Types:
1. single level inheritance.
2. multiple inheritance
3. multi level inheritance.
4. Hierarchical inheritance.
"""


class Car:
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
c1.set_audi_info()
# c1.base_info()
# c1.audi_info()
print("----------")
c1.show_full_info()
