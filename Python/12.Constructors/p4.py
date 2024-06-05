# 4. Write a program which illustrates the concept of attributes of a constructor.

class Person:
    def __init__(self, name, age):
        self.name = name  # Attribute: name
        self.age = age    # Attribute: age

# Creating an instance of Person class with attributes
person1 = Person("Alice", 30)

# Accessing and printing the attributes
print("Name:", person1.name)
print("Age:", person1.age)
