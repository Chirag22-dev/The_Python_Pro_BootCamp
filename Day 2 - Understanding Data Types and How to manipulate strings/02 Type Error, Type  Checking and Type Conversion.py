# len(12345) would give an error because:
# len() works only on objects that have length (like strings, lists, tuples),
# but integers do NOT have a length.

# -------------------------
# Type Checking
# -------------------------

# type() tells us the data type of a value

print(type("abc"))    # String type
print(type(123))      # Integer type
print(type(12.6))     # Float type
print(type(True))     # Boolean type

# -------------------------
# Type Conversion
# -------------------------

# "12" is a string, so we convert it to int before adding
# Otherwise Python would try string concatenation

print(int("12") + int("12"))  # Output: 24

# -------------------------
# Example Program
# -------------------------

# Taking user input (input() always returns a string)
name = input("Enter your name: ")

# len() counts the number of characters in the string
length = len(name)

# Convert length (int) to string before concatenating with text
print("Number of letters in your name: " + str(length))
