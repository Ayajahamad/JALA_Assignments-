# 1. Define a static variable and access that through a class 

class Employee:
    # static variable
    emp_name = "Jhon"

    def __init__(self):
        pass

# Accessing through class
static = Employee.emp_name
print(static)