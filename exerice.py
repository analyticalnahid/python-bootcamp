# 1. Email Validator

def is_valid_email(email):
    # Check if the email contains exactly one "@" symbol
    if email.count("@") != 1:
        return False

    # Split the email into username and domain parts
    username, domain = email.split("@")

    # Check if the username and domain are not empty
    if not username or not domain:
        return False

    # Check if the domain contains exactly one "."
    if domain.count(".") != 1:
        return False

    return True

user_email = input("Enter an email address: ")
if is_valid_email(user_email):
    print("The entered email address is valid.")
else:
    print("The entered email address is not valid.")

# 2. Palindrome Checker:

def is_palindrome(s):
    # Reverse the string using slicing
    reversed_s = s[::-1]
    # Compare the original string with the reversed string
    if s == reversed_s:
        return True  # If they are equal, the string is a palindrome
    return False  # If they are not equal, the string is not a palindrome

user_input = input("Enter a string: ")


if is_palindrome(user_input):
    print("The entered string is a palindrome.")
else:
    print("The entered string is not a palindrome.")

# 3. Password Generator:

import random
import string

def generate_password(length, use_lowercase, use_uppercase, use_digits):
    characters = ""
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits

    if not characters:
        return "Password cannot be generated without any character types selected."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("Password Generator")
print("------------------")

length = int(input("Enter the desired length of the password: "))
use_lowercase = input("Use lowercase letters? (y/n): ").lower() == 'y'
use_uppercase = input("Use uppercase letters? (y/n): ").lower() == 'y'
use_digits = input("Use digits? (y/n): ").lower() == 'y'

generated_password = generate_password(length, use_lowercase, use_uppercase, use_digits)
print("Generated Password:", generated_password)

