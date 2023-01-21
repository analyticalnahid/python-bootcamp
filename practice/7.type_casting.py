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


#bool(x): This function converts the value of x to a Boolean value (True or False).

x = 0
y = "hello"
z = []

a = bool(x)  # a is now False
b = bool(y)  # b is now True
c = bool(z)  # c is now False


#hex(x): This function converts the value of x to a hexadecimal string.

x = 10
y = 100

a = hex(x)  # a is now "0xA"
b = hex(y)  # b is now "0x64"


#oct(x): This function converts the value of x to an octal string.

x = 10
y = 100

a = oct(x)  # a is now "0o12"
b = oct(y)  # b is now "0o144"


#bin(x): This function converts the value of x to a binary string.

x = 10
y = 100

a = bin(x)  # a is now "0b1010"
b = bin(y)  # b is now "0b1100100"
