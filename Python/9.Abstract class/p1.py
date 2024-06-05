# 1. Create an abstract class with abstract and non-abstract methods

from abc import ABC, abstractmethod

# Abstract Class with Abstract and Non-Abstract Methods
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def habitat(self):
        pass

    def sleep(self):
        print("This animal is sleeping.")

# Subclasses Implementing Abstract Methods

class Dog(Animal):
    def sound(self):
        print("Bark")

    def habitat(self):
        print("Domestic")

class Bird(Animal):
    def sound(self):
        print("Chirp")

    def habitat(self):
        print("Forest")

# Using the Concrete Classes
def main():
    dog = Dog()
    bird = Bird()

    print("Dog:")
    dog.sound()        # Output: Bark
    dog.habitat()      # Output: Domestic
    dog.sleep()        # Output: This animal is sleeping.

    print("\nBird:")
    bird.sound()       # Output: Chirp
    bird.habitat()     # Output: Forest
    bird.sleep()       # Output: This animal is sleeping.

if __name__ == "__main__":
    main()

"""
Abstract Class (Animal):
Defines abstract methods (sound and habitat) that must be implemented by any subclass.
Includes a concrete method (sleep) that can be used by subclasses.

Concrete Subclasses (Dog and Bird):
Implement all abstract methods from the abstract class.
Can also use the concrete method defined in the abstract class.
"""