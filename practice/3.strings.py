# Simple String Value
name = "Alice"
print(name)

# String Concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)

# Formatted String
name = "Alice"
age = 30
print("My name is {} and I am {} years old.".format(name, age))

name = "John"
age = 30
print(f"My name is {name} and I am {age} years old.")


# Indexing and slicing to access parts of a string
word = "Python"
print(word[0])    
print(word[1:4]) 


# Repeat a string
repeated_string = "Hello " * 3
print(repeated_string) 


# Check substring of a string
text = "Python is a powerful programming language"
substring = "powerful"
print(substring in text)


"""              ________________________ String Method ________________________                   """


# Upper Case and Lower Case
text = "Welcome to the world of Python"
print(text.upper())   
print(text.lower())  
print(text.count("o")) 


string = "Python is a great programming language"
print(string.isupper()) 
print(string.islower()) 
string = "PYTHON IS A GREAT PROGRAMMING LANGUAGE"
print(string.isupper())
string = "python is a great programming language"
print(string.islower())


# Length of a string
sentence = "The quick brown fox jumps over the lazy dog."
print(len(sentence))

# Spliting String
sentence = "The quick brown fox jumps over the lazy dog"
words = sentence.split()
print(words) 

# Join List of Stirng into a single string
list_of_words = ["Python", "is", "a", "great", "language"]
string_of_words = " ".join(list_of_words)
print(string_of_words) 

# Remove whitespace from the beginning and end of a string
string_with_spaces = "     This is a string with spaces at the beginning and end    "
string_without_spaces = string_with_spaces.strip()
print(string_without_spaces)

# Replace a substring in a string
string_to_replace = "This is a test string"
replaced_string = string_to_replace.replace("test", "example")
print(replaced_string)

# Find the index of a substring
string = "Python is a great programming language"
substring = "great"
index = string.find(substring)
print(index)

# Check if a string starts or ends with a substring
string = "Python is a great programming language"
substring_start = "Python"
substring_end = "language"
print(string.startswith(substring_start)) 
print(string.endswith(substring_end))

# Change the capitalization of a string
string = "python is a great programming language"
print(string.capitalize())
print(string.title())

string = "Python Is A Great Programming Language"
print(string.istitle()) # Output: True
string = "Python is a great programming language"
print(string.istitle()) # Output: False

# Partion a string into of three parts
string = "Python is a great programming language"
print(string.partition("great"))

# Remove specific characters from a string
string = "!!Python is a great programming language!!"
stripped_string = string.strip("!")
print(stripped_string)

# Remove specific characters from the left or right side of a string
string = "!!Python is a great programming language!!"
stripped_left = string.lstrip("!")
stripped_right = string.rstrip("!")
print(stripped_left) 
print(stripped_right) 

# Check if a string contains only alphabetic characters
string = "Python"
print(string.isalpha()) 
string = "Python3"
print(string.isalpha())

# Method to format the string
person = {'name': 'Alice', 'age': 30}
string = "My name is {name} and I am {age} years old."
formatted_string = string.format_map(person)
print(formatted_string)

# Method to add leading zeroes to a string
string = "12"
zero_filled_string = string.zfill(4)
print(zero_filled_string)

# Check if a string contains only decimal characters
string = "123456"
print(string.isdecimal())
string = "123456abc"
print(string.isdecimal()) 

# Check if a string contains only digits
string = "123456"
print(string.isdigit()) 
string = "123456abc"
print(string.isdigit())

# Check if a string contains only numeric characters
string = "123456"
print(string.isnumeric()) # Output: True
string = "123456abc"
print(string.isnumeric()) # Output: False
string = "⅕"
print(string.isnumeric()) # Output: True

# String and fill with a specified character at right
string = "Python"
justified_string = string.rjust(10, "*")
print(justified_string)

# String and fill with a specified character at left
string = "Python"
justified_string = string.ljust(10, "*")
print(justified_string)

# String and fill with a specified character at center
string = "Python"
centered_string = string.center(10, "*")
print(centered_string)

# Swap the case of a string
string = "Python Is A Great Programming Language"
swapped_string = string.swapcase()
print(swapped_string)
