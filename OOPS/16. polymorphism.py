class Animal:
    def sound(self):
        print("Animal speaking")


class Dog(Animal):
    def sound(self):
        print("bhaw bhaw bhaw")


class Cat(Animal):
    def sound(self):
        print("meow meow meow")


obj = Dog()
obj.sound()
# This is method overriding in which first it will look in the dog class else it will look into the parent class of dog for the sound method if existig or not.

# Method overloading does not exist in python.
