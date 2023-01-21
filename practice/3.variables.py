
"""_______________________ 1. Value Assignment _______________________ """

# Declare a variable called "name" and assign it the string value "Alice"
name = "Alice"

# Declare a variable called "age" and assign it the integer value 25
age = 25

# Declare a variable called "city" and assign it the integer value Dhaka
city = "Dhaka"

# Declare a variable called "country" and assign it the integer value Bangladesh
country = "Bangladesh"

# Print the value of the "name" variable
print(name)
# Output: Alice

# Print the value of the "age" variable
print(age)
# Output: 25

# Print the value of the "city" variable
print(city)
# Output: Dhaka

# Print the value of the "country" variable
print(country)
# Output: Bangladesh



"""_______________________ 2. Value Re-Assignment _______________________ """


# Declare a variable called "name" and assign it the string value "Alice"
name = "Alice"

# Declare a variable called "age" and assign it the integer value 25
age = 25

# Print the value of the "name" variable
print(name)
# Output: Alice

# Print the value of the "age" variable
print(age)
# Output: 25

# Re-assign a new string value to the "name" variable
name = "Bob"

# Re-assign a new integer value to the "age" variable
age = 30

# Print the value of the "name" variable again
print(name)
# Output: Bob

# Print the value of the "age" variable again
print(age)
# Output: 30


"""_______________________ 3. Assigning a single value to multiple variables _______________________ """



# Declare three variables: "a", "b", and "c"
a, b, c = 500

# Print the values of the variables
print(a)
# Output: 500
print(b)
# Output: 500
print(c)
# Output: 500

# Re-assign the same value to all three variables
a, b, c = 100

# Print the values of the variables again
print(a)
# Output: 100
print(b)
# Output: 100
print(c)
# Output: 100



"""_______________________ 4. Assigning multiple value to multiple variables _______________________ """



# Declare three variables: "a", "b", and "c"
a, b, c = 10, 20, 30

# Print the values of the variables
print(a)
# Output: 10
print(b)
# Output: 20
print(c)
# Output: 30

# Re-assign different values to the variables
a, b, c = 100, 200, 300

# Print the values of the variables again
print(a)
# Output: 100
print(b)
# Output: 200
print(c)
# Output: 300


"""_______________________ 5. Delete multiple variables _______________________ """


# Declare three variables: "a", "b", and "c"
a, b, c = 10, 20, 30

# Print the values of the variables
print(a)
# Output: 10
print(b)
# Output: 20
print(c)
# Output: 30

# Delete the "b" and "c" variables
del b
del c

# Try to print the values of the "b" and "c" variables
print(b)
# Output: NameError: name 'b' is not defined
print(c)
# Output: NameError: name 'c' is not defined

# The "a" variable still exists and can be accessed
print(a)
# Output: 10

