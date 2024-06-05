# 2. Create a sub class for an abstract class. Create an object in the child class for the abstract class and access the non-abstract methods


from abc import ABC, abstractmethod

# Abstract Class with Non-Abstract Methods
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def habitat(self):
        pass

    def sleep(self):
        print("This animal is sleeping.")  # Non-abstract method

# Subclass Implementing Abstract Methods
class Dog(Animal):
    def sound(self):
        return "Bark"

    def habitat(self):
        return "Domestic"

# Creating Object in the Child Class and Accessing Non-Abstract Methods
def main():
    dog = Dog()

    print("Dog:")
    print("Sound:", dog.sound())      # Output: Bark
    print("Habitat:", dog.habitat())  # Output: Domestic
    dog.sleep()                       # Output: This animal is sleeping.

if __name__ == "__main__":
    main()

