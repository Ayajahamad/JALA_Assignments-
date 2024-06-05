# 2. Define a static variable and access that through a instance

class Employee:
    # static variable
    emp_name = "Jhon"

    def __init__(self):
        pass

# Accessing through instance
obj = Employee()
inst = obj.emp_name
print(inst)
