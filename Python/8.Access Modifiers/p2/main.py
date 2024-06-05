# main.py

from packege1.Baseclass import BaseClass, AnotherClassInSamePackage
from packege2.Childclass import ChildClass, AnotherClassInDifferentPackage

def main():
    # Access from within the class itself
    base_obj = BaseClass(50, 60)
    base_obj.main_method()

    # Access from another class in the same package
    another_class_same_package = AnotherClassInSamePackage()
    another_class_same_package.access_protected_members()

    # Access from a child class in a different package
    child_obj = ChildClass(70, 80)
    child_obj.access_protected_from_child()

    # Access from another class in a different package
    another_class_diff_package = AnotherClassInDifferentPackage()
    another_class_diff_package.access_protected_members()

if __name__ == "__main__":
    main()
