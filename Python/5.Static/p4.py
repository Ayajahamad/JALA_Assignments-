# 4. Define a static variable and change within the class

class MyClass:
    static_var = 10

    @classmethod
    def chnge_static(cls,value):
        cls.static_var = value


print(MyClass.static_var) # Befor chnaging

MyClass.chnge_static(20)
print(MyClass.static_var) # After changing


