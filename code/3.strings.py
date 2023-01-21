
# Simple String Value
name = "Alice"
print(name)

cName = str("Bangladesh")
print(cName)


# String Concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)

# Formatted String
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

