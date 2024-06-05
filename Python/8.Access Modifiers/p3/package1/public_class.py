# package1/public_class.py

class PublicClass:
    def __init__(self, value1, value2):
        self.public_field1 = value1  # Public field
        self.public_field2 = value2  # Public field

    def public_method(self):
        print(f"Public method called! Values: {self.public_field1}, {self.public_field2}")

# Accessing public members from another class in the same package
class AnotherClassInSamePackage:
    def access_public_members(self):
        obj = PublicClass(10, 20)
        print(f"Accessing public fields from AnotherClassInSamePackage: {obj.public_field1}, {obj.public_field2}")
        obj.public_method()
