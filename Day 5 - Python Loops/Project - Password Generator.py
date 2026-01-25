import random

# List containing all uppercase and lowercase letters
letters = [
    'A','B','C','D','E','F','G','H','I','J',
    'K','L','M','N','O','P','Q','R','S','T',
    'U','V','W','X','Y','Z',
    'a','b','c','d','e','f','g','h','i','j',
    'k','l','m','n','o','p','q','r','s','t',
    'u','v','w','x','y','z'
]

# List containing digits as strings
numbers = ['0','1','2','3','4','5','6','7','8','9']

# List containing special symbols
symbols = [
    '(', ')', '[', ']', '{', '}',
    '<', '>',
    '|', '\\'
]

# Welcome message
print("Welcome to the Password Generator!")

# User input for number of characters
num_letters = int(input("How many letters would you like? "))
num_numbers = int(input("How many numbers would you like? "))
num_symbols = int(input("How many symbols would you like? "))


# ------------------------
# Easy Way
# ------------------------
# Generates password in a fixed order:
# letters -> numbers -> symbols

# password = ""
# for char in range(0, num_letters):
#     password += random.choice(letters)
#
# for char in range(0, num_numbers):
#     password += random.choice(numbers)
#
# for char in range(0, num_symbols):
#     password += random.choice(symbols)
#
# print(password)


# ------------------------
# Hard Way
# ------------------------
# Generates password with randomized order (more secure)

# Empty list to store password characters
password_list = []

# Add random letters to the list
for char in range(0, num_letters):
    password_list += random.choice(letters)

# Add random numbers to the list
for char in range(0, num_numbers):
    password_list += random.choice(numbers)

# Add random symbols to the list
for char in range(0, num_symbols):
    password_list += random.choice(symbols)

# Shuffle the list to randomize character order
random.shuffle(password_list)

# Print the password list (for understanding/debugging)
print(password_list)

# Convert the list into a string
password = ""

# Join each character to form the final password
for char in password_list:
    password += char

# Print the final generated password
print(password)
