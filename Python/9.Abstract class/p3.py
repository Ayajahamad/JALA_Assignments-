# 3. Create an instance for the child class in child class and call abstract methods.

from abc import ABC, abstractmethod

class Animal:

    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def habitat(self):
        pass

    def sleep(self):
        print("Animal is Sleeping")

class Dog(Animal):
    def sound(self):
        print("Bark..")

    def habitat(self):
        print("Domestic..")
    
    def call_abstract_method(self):
        # creating instance
        instance = Dog()
        # calling abstract methods
        instance.sound()
        instance.habitat()

def main():
    dog = Dog()
    dog.call_abstract_method()

if __name__=="__main__":
    main()
