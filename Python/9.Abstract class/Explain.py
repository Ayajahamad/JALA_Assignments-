"""
In Python, an abstract class is a class that cannot be instantiated on its own and is meant to be subclassed. Abstract classes often contain one or more abstract methods, which are methods declared in an abstract class but do not have an implementation. Abstract classes in Python are defined using the `abc` (Abstract Base Classes) module, which is part of Python's standard library.

Here’s a comprehensive overview of abstract classes in Python:

### 1. Abstract Base Classes (ABCs)
Abstract Base Classes are classes that are designed to be a base for other classes. They provide a way to define a common interface for a set of subclasses. 

### 2. Importing the `abc` module
To use abstract classes in Python, you need to import the `ABC` class and the `abstractmethod` decorator from the `abc` module.

```python
from abc import ABC, abstractmethod
```

### 3. Defining an Abstract Class
An abstract class is defined by inheriting from the `ABC` class. Within this class, you can define abstract methods using the `@abstractmethod` decorator.

#### Example:
```python
from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

    @abstractmethod
    def another_abstract_method(self):
        pass
```

### 4. Concrete Methods in Abstract Classes
Abstract classes can also contain concrete methods, which have an implementation. These methods can be used by subclasses.

#### Example:
```python
class AbstractClassWithConcreteMethod(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

    def concrete_method(self):
        print("This is a concrete method.")
```

### 5. Creating Subclasses
Subclasses of an abstract class must implement all abstract methods. If a subclass does not implement all abstract methods, it will also be considered abstract and cannot be instantiated.

#### Example:
```python
class ConcreteClass(AbstractClass):
    def abstract_method(self):
        print("Implementation of abstract_method")

    def another_abstract_method(self):
        print("Implementation of another_abstract_method")
```

### 6. Instantiating Classes
You cannot instantiate an abstract class directly. Attempting to do so will raise a `TypeError`.

#### Example:
```python
try:
    obj = AbstractClass()
except TypeError as e:
    print(e)  # Output: Can't instantiate abstract class AbstractClass with abstract methods abstract_method, another_abstract_method
```

### 7. Example with Abstract and Concrete Methods
Let's combine the above concepts into a complete example.
"""


from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    def sleep(self):
        print("Sleeping...")

class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

# Attempt to instantiate an abstract class
try:
    animal = Animal()
except TypeError as e:
    print(e)  # Output: Can't instantiate abstract class Animal with abstract method make_sound

# Create instances of concrete classes
dog = Dog()
cat = Cat()

dog.make_sound()  # Output: Bark
cat.make_sound()  # Output: Meow
dog.sleep()       # Output: Sleeping...
cat.sleep()       # Output: Sleeping...

"""
### 8. Advantages of Abstract Classes
- **Encapsulation of Interface**: They provide a way to define a common interface for all subclasses.
- **Enforcement**: Ensures that subclasses implement specific methods.
- **Code Reusability**: Allows for code reuse by defining concrete methods in the abstract class.

### 9. Use Cases for Abstract Classes
- **Framework Design**: When designing frameworks where you want to enforce certain patterns on how the classes are implemented.
- **API Design**: To ensure that certain methods are implemented in API-related classes.
- **Large Projects**: In large codebases, to maintain consistency and enforce a common interface across different parts of the system.

### Summary
- **Abstract Classes**: Cannot be instantiated directly and are meant to be subclassed.
- **Abstract Methods**: Methods that are declared but not implemented in the abstract class. Subclasses must implement these methods.
- **Concrete Methods**: Regular methods with implementations that can be used by subclasses.
- **abc Module**: Used to create abstract classes and methods in Python.

By understanding and using abstract classes, you can design more robust and maintainable code by enforcing a common interface and behavior across related classes.
"""