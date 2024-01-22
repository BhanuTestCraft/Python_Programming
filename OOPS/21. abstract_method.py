from abc import ABC, abstractmethod


class Car(ABC):
    # Here we want this sound method should be compulsary in each of the inherited class so we use the abstract method here. It is not allowed to create the abstract class object so no will call this calss so we have written the pass statement in sound method.
    @abstractmethod
    def sound(self):
        print("abc")
        pass


class Audi(Car):
    def __init__(self, engine) -> None:
        self.engine = engine

    def sound(self):
        print("SPORTS SOUND")


# obj = Car()
# output: TypeError: Can't instantiate abstract class Car with abstract method sound
obj = Audi("1200cc")
obj.sound()
