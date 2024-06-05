# package2/child_class.py

from packege1.Baseclass import BaseClass

class ChildClass(BaseClass):
    def access_protected_from_child(self):
        # Accessing protected fields and methods from subclass
        print(f"Accessing protected fields from ChildClass: {self._protected_field1}, {self._protected_field2}")
        self._protected_method()

# Accessing protected members from another class in a different package
class AnotherClassInDifferentPackage:
    def access_protected_members(self):
        obj = BaseClass(30, 40)
        print(f"Accessing protected fields from AnotherClassInDifferentPackage: {obj._protected_field1}, {obj._protected_field2}")
        obj._protected_method()
