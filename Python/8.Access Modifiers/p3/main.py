# main.py

from package1.public_class import PublicClass, AnotherClassInSamePackage
from package2.another_class import AnotherClassInDifferentPackage

def main():
    # Access from within the same class
    public_obj = PublicClass(50, 60)
    public_obj.public_method()

    # Access from another class in the same package
    another_class_same_package = AnotherClassInSamePackage()
    another_class_same_package.access_public_members()

    # Access from another class in a different package
    another_class_diff_package = AnotherClassInDifferentPackage()
    another_class_diff_package.access_public_members()

if __name__ == "__main__":
    main()
