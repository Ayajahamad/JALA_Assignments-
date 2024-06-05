# 2. Write a method for increment and decrement operators(++, --)

def incrementOpe(value):
    print(f"The actual value : {value}")
    return f"Value After Incrementing = {value+1}"
    
def decrementOpe(value):
    print(f"The actual value : {value}")
    return f"Value After Decrement = {value-1}"


inc = incrementOpe(2)
print(inc)

dec = decrementOpe(2)
print(dec)



# Equivalent for i
i = 5
i += 1  # Post-increment equivalent: i becomes 6
i += 1  # Pre-increment equivalent: i becomes 7

# Equivalent for j
j = 5
j -= 1  # Post-decrement equivalent: j becomes 4
j -= 1  # Pre-decrement equivalent: j becomes 3

# Print the results to verify
print("i =", i)  # Output: i = 7
print("j =", j)  # Output: j = 3
