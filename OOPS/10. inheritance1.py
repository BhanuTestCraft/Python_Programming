"""
Inheritance means inheriting something from base class.
car prop: color, type, mileage, seat capacity
audi: color, type, mileage, seat capacity, branch, city
maruti: color, type, mileage, seat capacity, ....
"""


class Car:
    # creating initialiser for the class.
    def __init__(
        self, color: str, type: str, mileage: float, seat_capacity: int
    ) -> None:
        self.color = color
        self.type = type
        self.mileage = mileage
        self.seat_capacity = seat_capacity

    def base_info(self):
        print(f"color = {self.color}")
        print(f"type = {self.type}")
        print(f"mileage = {self.mileage}")
        print(f"seat_capacity = {self.seat_capacity}")


class Audi(Car):
    def __init__(self) -> None:
        print("Audi INIT")


# c1 = Car("Black", "Petrol", 25.5, 5)
# c1.base_info()

c1 = Audi()
c1.color = "Black"
c1.type = "Petrol"
c1.mileage = 21
c1.seat_capacity = 7
c1.base_info()
