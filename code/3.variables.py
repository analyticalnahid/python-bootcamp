# value assigning
name = "Python"

# object reference
print(type(name))


# object identity
name1 = "Hello 1"
name2 = "Hello 2"
print(id(name1))
print(id(name2))

# value re-assigning
name = "Python 3.11"

# Assigning a single value to multiple variables
a = b = c = 10

# Assigning different values to multiple variables
a, b, c = 1, 20.2, "GeeksforGeeks"

# output to consloe
print(name)

# local variable
def hello():
  local = "I am local variable"

# delete a variable  
del a

# This will raise an error, as the variable a has been deleted
print(x)
