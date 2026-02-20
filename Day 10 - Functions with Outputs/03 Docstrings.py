# Function to format full name with proper capitalization
def full_name(fname, lname):
    """Docstring for documenting"""

    # Check if either first name or last name is empty
    # If any input is empty, return None (implicit return)
    if fname == "" or lname == "":
        return

    # Convert first name to title case (capitalize first letter)
    formatted_fname = fname.title()

    # Convert last name to title case
    formatted_lname = lname.title()

    # Return the properly formatted full name using f-string
    return f"{formatted_fname} {formatted_lname}"


# Call the function and print the result
print(full_name("John", "Doe"))