# 1. Write two methods with the same name but different number of parameters of same type and call the methods.

"""
Method Overloading:

Two or more methods have the same name but different numbers of parameters or different types of parameters, or both. These methods are called overloaded methods and this is called method overloading. 

Like other languages (for example, method overloading in C++) do, python does not support method overloading by default. But there are different ways to achieve method overloading in Python. 

The problem with method overloading in Python is that we may overload the methods but can only use the latest defined method.
"""

# First product method.
# Takes two argument and print their
# product


def product(a, b):
	p = a * b
	print(p)

# Second product method
# Takes three argument and print their
# product


def product(a, b, c):
	p = a * b*c
	print(p)

# Uncommenting the below line shows an error
# product(4, 5)

# This line will call the second product method
product(4, 5, 5)



## Defining Method Overloading


print("Method Overloading in Python..! ")
# Function to take multiple arguments
def add(datatype, *args):
	
	# if datatype is int
	# initialize answer as 0
	if datatype == 'int':
		answer = 0

	# if datatype is str
	# initialize answer as ''
	if datatype == 'str':
		answer = ''

	# Traverse through the arguments
	for x in args:

		# This will do addition if the
		# arguments are int. Or concatenation
		# if the arguments are str
		answer = answer + x
	print(answer)

# Integer
add('int', 5, 6)

# String
add('str', 'Hi ', 'Geeks')


