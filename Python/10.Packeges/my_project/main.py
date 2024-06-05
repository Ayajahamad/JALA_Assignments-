# main.py
from my_package import Class1, Class2

def main():
    # Create instances of each class
    obj1 = Class1("Hello from Class1")
    obj2 = Class2("Hello from Class2")

    # Call the display method of each instance
    obj1.display()
    obj2.display()

if __name__ == "__main__":
    main()
