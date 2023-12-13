import re

def is_valid_password(password):

    if len(password) < 8:
        return False

    if not password.isalnum():
        return False

    digit_count = sum(1 for char in password if char.isdigit())
    if digit_count < 2:
        return False

    return True

# Test the function with a password
password = input("Enter a password: ")

if is_valid_password(password):
    print("Valid password.")
else:
    print("Invalid password.")