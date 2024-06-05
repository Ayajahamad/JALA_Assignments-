# 2. Write two methods with the same name but different number of parameters of different data type and call the methods 

class Example:
    def display(self, arg1, arg2=None):
        if arg2 is None:
            self._display_one(arg1)
        else:
            self._display_two(arg1, arg2)

    def _display_one(self, arg):
        if isinstance(arg, int):
            print(f"One integer argument: {arg}")
        elif isinstance(arg, str):
            print(f"One string argument: '{arg}'")
        else:
            print("Unsupported argument type")

    def _display_two(self, arg1, arg2):
        if isinstance(arg1, int) and isinstance(arg2, str):
            print(f"Two arguments of different types: {arg1}, '{arg2}'")
        elif isinstance(arg1, str) and isinstance(arg2, int):
            print(f"Two arguments of different types: '{arg1}', {arg2}")
        else:
            print("Unsupported argument types")

# Creating an instance of the Example class
obj = Example()

# Calling the display method with different numbers of parameters and data types
obj.display(5)          # Output: One integer argument: 5
obj.display("hello")    # Output: One string argument: 'hello'
obj.display(5, "world") # Output: Two arguments of different types: 5, 'world'
obj.display("world", 5) # Output: Two arguments of different types: 'world', 5
