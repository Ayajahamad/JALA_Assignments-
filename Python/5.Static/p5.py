# Static and instance

class MyClass:
    # Static (class) variable
    static_var = 0

    def __init__(self, value):
        # Instance variable
        self.instance_var = value

    def increment_static(self):
        # Modify the static variable
        MyClass.static_var += 1

    def increment_instance(self):
        # Modify the instance variable
        self.instance_var += 1

    @classmethod
    def set_static(cls, value):
        # Set the static variable using class method
        cls.static_var = value

    def display(self):
        # Display the instance and static variables
        print(f'Instance Variable: {self.instance_var}, Static Variable: {MyClass.static_var}')


# Create instances of MyClass
obj1 = MyClass(10)
obj2 = MyClass(20)

# Access and display initial values
obj1.display()  # Output: Instance Variable: 10, Static Variable: 0
obj2.display()  # Output: Instance Variable: 20, Static Variable: 0

# Increment static variable using an instance method
obj1.increment_static()

# Increment instance variable using an instance method
obj1.increment_instance()

# Display values after incrementing
obj1.display()  # Output: Instance Variable: 11, Static Variable: 1
obj2.display()  # Output: Instance Variable: 20, Static Variable: 1

# Set static variable using a class method
MyClass.set_static(5)

# Display values after setting static variable
obj1.display()  # Output: Instance Variable: 11, Static Variable: 5
obj2.display()  # Output: Instance Variable: 20, Static Variable: 5
