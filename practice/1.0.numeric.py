
# Operation with integers
a = 3 + 2
b = 3 * 3

print(a)
print(b)


"""              ________________________ Integers Method ________________________                   """






# The absolute value of an integer
x = -5
y = abs(x)
print(y) 

# The quotient and remainder of a division operation
x = 7
y = 3
quotient, remainder = divmod(x, y)
print(quotient) 
print(remainder)

# Raise an integer to a power
x = 2
y = 3
z = pow(x, y)
print(z)

# Round an integer to a specified number of decimal places
x = 2.7
y = round(x)
print(y)

# An integer to a binary, octal, or hexadecimal string respectively
x = 15
print(bin(x)) 
print(oct(x)) 
print(hex(x))

# The sum of a list of integers
x = [1, 2, 3, 4, 5]
y = sum(x)
print(y)

# The max number of a list of integers
x = [1, 2, 3, 4, 5]
y = max(x)
print(y)

# The min number of a list of integers
x = [1, 2, 3, 4, 5]
y = min(x)
print(y)

# Generating random number
import random
print(random.randrange(1, 10)) 

