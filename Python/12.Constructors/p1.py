# 1. Write a class with a default constructor, one argument constructor and two argument constructors. Instantiate the class to call all the constructors of that class from a main class

class MyClass:
    def __init__(self, arg1=None, arg2=None):
        if arg1 is None and arg2 is None:
            print("Default constructor called")
        elif arg2 is None:
            print(f"One-argument constructor called with arg1={arg1}")
        else:
            print(f"Two-argument constructor called with arg1={arg1} and arg2={arg2}")

class MainClass:
    def __init__(self):
        print("Calling constructors of MyClass:")
        # Calling default constructor
        instance1 = MyClass()
        # Calling one-argument constructor
        instance2 = MyClass("Value1")
        # Calling two-argument constructor
        instance3 = MyClass("Value1", "Value2")

# Instantiate MainClass to call the constructors
main_instance = MainClass()
