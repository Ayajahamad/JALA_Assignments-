class A:
    def __init__(self):
        self.value = "Value from class A"

    def method_a1(self):
        print("Method A1 from class A")

    def method_a2(self):
        print("Method A2 from class A")

    def override_method(self):
        print("Override method in class A")


class B(A):
    def __init__(self):
        super().__init__()
        self.value = "Value from class B"

    def method_b1(self):
        print("Method B1 from class B")

    def method_b2(self):
        print("Method B2 from class B")

    def override_method(self):
        print("Override method in class B")


class C(B):
    def __init__(self):
        super().__init__()
        self.value = "Value from class C"

    def method_c1(self):
        print("Method C1 from class C")

    def method_c2(self):
        print("Method C2 from class C")

    def override_method(self):
        print("Override method in class C")


# Main method to create instances and call methods
def main():
    # Creating objects for each class
    obj_a = A()
    obj_b = B()
    obj_c = C()

    # Calling methods of class A
    print("Methods of class A:")
    obj_a.method_a1()
    obj_a.method_a2()
    obj_a.override_method()
    print()

    # Calling methods of class B
    print("Methods of class B:")
    obj_b.method_b1()
    obj_b.method_b2()
    obj_b.override_method()
    print()

    # Calling methods of class C
    print("Methods of class C:")
    obj_c.method_c1()
    obj_c.method_c2()
    obj_c.override_method()
    print()

    # Demonstrating runtime polymorphism with method overriding
    print("Runtime Polymorphism with method overriding:")
    a_ref_b = obj_b  # Super class reference to sub class object
    a_ref_c = obj_c  # Super class reference to sub class object
    a_ref_b.override_method()
    a_ref_c.override_method()
    print()

    # Runtime Polymorphism with Data Members
    print("Runtime Polymorphism with data members:")
    print(f"Value in class A object: {obj_a.value}")
    print(f"Value in class B object: {obj_b.value}")
    print(f"Value in class C object: {obj_c.value}")
    print()

    a_ref_b = obj_b  # Super class reference to sub class object
    a_ref_c = obj_c  # Super class reference to sub class object
    print(f"Value in class A reference to B object: {a_ref_b.value}")
    print(f"Value in class A reference to C object: {a_ref_c.value}")


if __name__ == "__main__":
    main()
