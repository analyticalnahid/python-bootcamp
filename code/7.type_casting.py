"""Implicit Type Conversion"""

x = 10
y = 5.5

z = x + y
print(z)  # Output: 15.5



"""Explicit Type Conversion"""

#int(x): This function converts the value of x to an integer. If x is a floating-point number, it will be truncated to an integer.

x = 10.5
y = "20"

a = int(x)  # a is now 10
b = int(y)  # b is now 20


#float(x): This function converts the value of x to a floating-point number.

x = 10
y = "20.5"

a = float(x)  # a is now 10.0
b = float(y)  # b is now 20.5


#str(x): This function converts the value of x to a string.

x = 10
y = 20.5

a = str(x)  # a is now "10"
b = str(y)  # b is now "20.5"

