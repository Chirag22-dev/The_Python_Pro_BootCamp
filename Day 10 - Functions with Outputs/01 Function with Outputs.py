# Function to format first name and last name properly
def full_name(fname, lname):
    # Convert first name to title case (First letter capitalized)
    formatted_fname = fname.title()

    # Convert last name to title case
    formatted_lname = lname.title()

    # Return full name with space in between
    return formatted_fname + " " + formatted_lname


# Calling the full_name function and printing the result
print(full_name("John", "Doe"))


# Function that duplicates the given text
def function1(text):
    # Returns the text repeated twice
    return text + text


# Function that converts text into title case
def function2(text):
    # Returns text with first letter capitalized
    return text.title()


# Nested function call:
# First function1("toyota") → "toyotatoyota"
# Then function2(...) → "Toyotatoyota"
print(function2(function1("toyota")))