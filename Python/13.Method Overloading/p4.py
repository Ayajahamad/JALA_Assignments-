class Example:
    def display(self, *args, **kwargs):
        if args and kwargs:
            print(f"Positional arguments: {args}, Keyword arguments: {kwargs}")
        elif args:
            print(f"Positional arguments: {args}")
        elif kwargs:
            print(f"Keyword arguments: {kwargs}")
        else:
            print("No arguments passed")

obj = Example()
obj.display()                    # No arguments passed
obj.display(1, 2, 3)             # Positional arguments: (1, 2, 3)
obj.display(a=1, b=2)            # Keyword arguments: {'a': 1, 'b': 2}
obj.display(1, 2, a=1, b=2)      # Positional arguments: (1, 2), Keyword arguments: {'a': 1, 'b': 2}