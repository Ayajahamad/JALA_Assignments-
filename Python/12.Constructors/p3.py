# 3. Apply private, public, protected and default access modifiers to the constructor

class MyClass:
    def __init__(self):
        print("Public constructor called")

class _ProtectedClass:
    def __init__(self):
        print("Protected constructor called")

class __PrivateClass:  # Name mangling to simulate private access
    def __init__(self):
        print("Private constructor called")
    
# Default
class MyClass1:
    pass  # No explicit constructor defined
# Creating an instance of MyClass
obj = MyClass1()


# Creating instances of the classes
obj1 = MyClass()
obj2 = _ProtectedClass()
obj3 = __PrivateClass()
