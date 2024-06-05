# 2. Call the constructors(both default and argument constructors) of super class from a child class

class SuperClass:
    def __init__(self, arg1=None, arg2=None):
        if arg1 is None and arg2 is None:
            print("Default constructor of SuperClass called")
        elif arg2 is None:
            print(f"One-argument constructor of SuperClass called with arg1={arg1}")
        else:
            print(f"Two-argument constructor of SuperClass called with arg1={arg1} and arg2={arg2}")

class ChildClass(SuperClass):
    def __init__(self, arg1=None, arg2=None):
        print("Constructor of ChildClass called")
        super().__init__(arg1, arg2)  # Call superclass constructor

# Create an instance of ChildClass
# Calling default
child = ChildClass()

# Calling with one-argument
child2 = ChildClass("value1")