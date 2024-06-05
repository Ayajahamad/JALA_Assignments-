# 3. Write two methods with the same name and same number of parameters of same type
"""

class Example:
    def display(self, arg):
        print("Calling display method")

    def display(self, arg):
        print(f"Displaying: {arg}")

# Creating an instance of the Example class
obj = Example()

# Calling the display method with different arguments
obj.display(5)        # Output: Calling display method
                      #         Displaying: 5

obj.display(10)  # Output: Calling display method
                      #         Displaying: hello

"""



## Achiving in python

class Example:
    def display(self, arg):
        if isinstance(arg, int):
            self._display(arg)
        elif isinstance(arg, str):
            self._display(arg)
        else:
            print("Unsupported argument type")

    def _display(self, arg):
        print(f"Displaying: {arg}")

# Creating an instance of the Example class
obj = Example()

# Calling the display method with different types of arguments
obj.display(5)          # Output: Displaying: 5
obj.display("hello")    # Output: Displaying: hello
obj.display(2.90)    # Output: Unsupported argument type
