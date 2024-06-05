# package1/base_class.py

class BaseClass:
    def __init__(self, value1, value2):
        self._protected_field1 = value1  # Protected field
        self._protected_field2 = value2  # Protected field

    def _protected_method(self):
        print(f"Protected method called! Values: {self._protected_field1}, {self._protected_field2}")

    def main_method(self):
        # Accessing protected fields within the class
        print(f"Accessing protected fields in main method: {self._protected_field1}, {self._protected_field2}")
        # Calling protected method within the class
        self._protected_method()

# Accessing protected members from another class in the same package
class AnotherClassInSamePackage:
    def access_protected_members(self):
        obj = BaseClass(10, 20)
        print(f"Accessing protected fields from AnotherClassInSamePackage: {obj._protected_field1}, {obj._protected_field2}")
        obj._protected_method()


"""
Protected members: In Python, protected members (with a single underscore) are accessible within the class, from subclasses, and from other classes within the same package. While they can also be accessed from other packages, this is generally discouraged and should be avoided to maintain encapsulation principles.
"""