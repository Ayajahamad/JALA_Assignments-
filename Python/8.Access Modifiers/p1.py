class BaseClass:
    def __init__(self, value1, value2):
        self.__private_field1 = value1  # Private field
        self.__private_field2 = value2  # Private field

    def __private_method(self):
        print(f"Private method called! Values: {self.__private_field1}, {self.__private_field2}")

    def main_method(self):
        # Accessing private fields within the class
        print(f"Accessing private fields in main method: {self.__private_field1}, {self.__private_field2}")
        # Calling private method within the class
        self.__private_method()
        
# Create an instance of BaseClass and call main_method
base_obj = BaseClass(10, 20)
base_obj.main_method()


# Subclass definition
class SubClass(BaseClass):
    def access_private_fields_and_methods(self):
        try:
            print(self.__private_field1)  # Attempt to access private field
        except AttributeError:
            print("Cannot access private field __private_field1 from subclass")

        try:
            print(self.__private_field2)  # Attempt to access private field
        except AttributeError:
            print("Cannot access private field __private_field2 from subclass")

        try:
            self.__private_method()  # Attempt to call private method
        except AttributeError:
            print("Cannot call private method __private_method from subclass")

# Create an instance of SubClass and attempt to access private fields and methods
sub_obj = SubClass(30, 40)
sub_obj.access_private_fields_and_methods()
