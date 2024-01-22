class Car:
    """
    Represents a generic car.

    Attributes:
    - color (str): The color of the car.
    - model (str): The model of the car.
    - mileage (float): The mileage of the car.
    - seat_capacity (int): The seating capacity of the car.
    """

    def set_info(
        self, color: str, model: str, mileage: float, seat_capacity: int
    ) -> None:
        """
        Set the basic information of the car.

        Parameters:
        - color (str): The color of the car.
        - model (str): The model of the car.
        - mileage (float): The mileage of the car.
        - seat_capacity (int): The seating capacity of the car.
        """
        self.color = color
        self.model = model
        self.mileage = mileage
        self.seat_capacity = seat_capacity

    def base_info(self) -> None:
        """Print the basic information of the car."""
        print(f"Color: {self.color}")
        print(f"Model: {self.model}")
        print(f"Mileage: {self.mileage}")
        print(f"Seat Capacity: {self.seat_capacity}")


class Audi(Car):
    """
    Represents an Audi car, inheriting from the Car class.

    Attributes:
    - electric (bool): Indicates if the Audi car is electric.
    - city (str): The city where the Audi car is located.
    """

    def set_audi_info(self, electric: bool, city: str) -> None:
        """
        Set additional information specific to Audi cars.

        Parameters:
        - electric (bool): Indicates if the Audi car is electric.
        - city (str): The city where the Audi car is located.
        """
        self.electric = electric
        self.city = city

    def audi_info(self) -> None:
        """Print additional information specific to Audi cars."""
        print(f"Electric: {self.electric}")
        print(f"City: {self.city}")


# Example usage:
c1 = Audi()
c1.set_info("Black", "A4", 17.5, 5)
c1.set_audi_info(True, "Mumbai")
c1.base_info()
c1.audi_info()
