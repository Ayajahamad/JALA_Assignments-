# 12. Write a program to generate NoSuchFieldException

"""
In Python, there is no direct equivalent to the NoSuchFieldException in Java, as Python is a dynamically-typed language and does not have the concept of fields in the same way that Java does.

However, you can simulate a similar scenario by attempting to access an attribute that does not exist within an object or class. This would typically result in an AttributeError being raised."""


class MyClass:
    def __init__(self):
        self.field1 = 10

def generate_no_such_field_exception(obj):
    try:
        # Attempting to access a non-existent attribute
        print(obj.field2)
    except AttributeError:
        raise AttributeError("No such field!")

def main():
    try:
        my_object = MyClass()
        generate_no_such_field_exception(my_object)
    except AttributeError as e:
        print("Error:", e)

# Main block
if __name__ == "__main__":
    main()
