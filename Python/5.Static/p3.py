# 3. Define a static variable and change within the instance

class Employee:
    static_var = "Jhon"

    def __init__(self):
        pass

    def change_static_var(self,new_val):
        self.static_var = new_val

obj = Employee()
print(f"Static var Before Changing : {obj.static_var}")


# chnaging static var
obj.change_static_var("Makram")
print(f"Static var After Changing : {obj.static_var}")

