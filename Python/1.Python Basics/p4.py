# 4. Define the local and Global variables with the same name and print both variables and understand the scope of the variables.

# Global variable
my_variable = "Global"

def my_function():
    # Local variable with the same name as the global variable
    my_variable = "Local"
    
    # Print local variable
    print("Inside the function, my_variable is:", my_variable)

# Call the function
my_function()

# Print global variable
print("Outside the function, my_variable is:", my_variable)


"""
    Global variables are accessible throughout the entire program.
    Local variables are only accessible within the function or block of code where they are defined. If a local variable has the same name as a global variable, the local variable shadows the global variable within its scope.
"""