

# Identity operator examples

x = [1, 2, 3]
y = [1, 2, 3]
z = x

# Check if two variables refer to the same object
print(x is y)   # False
print(x is z)   # True

# Check if two variables do not refer to the same object
print(x is not y)   # True
print(x is not z)   # False



"""Difference between is and == """

x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)   # True
print(x is y)   # False
