# package2/another_class.py

from package1.public_class import PublicClass

class AnotherClassInDifferentPackage:
    def access_public_members(self):
        obj = PublicClass(30, 40)
        print(f"Accessing public fields from AnotherClassInDifferentPackage: {obj.public_field1}, {obj.public_field2}")
        obj.public_method()
