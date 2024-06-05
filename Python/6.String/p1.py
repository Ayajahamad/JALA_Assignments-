# 1. Different ways creating a string

# 1. Using Single Quote
str1 = 'Hello, World'
print(str1)

# 2. Using Double Quote
str2 = "Hello, World"
print(str2)

# 3. Using Triple Quote(single/Double) / Multiline String
str3 = """Hello, 
World"""
print(str3)

# 4. Using 'str()' Function
num1 = 123
str4 = str(num1)
print(type(str4) , str4)

# 5. Using Concatination
st1 = "hello,"
st2 = "world"
concatinated_str = st1+st2+" Another"
print(concatinated_str)

# 6. Raw string
raw_string = r"C:\Users\name"
print(raw_string)  # Output: C:\Users\name
