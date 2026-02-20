# Function to format full name properly
def full_name(fname, lname):
    # Check if either first name or last name is empty
    # If any one is empty, return None (no value)
    if fname == "" or lname == "":
        return

    # Convert first name to title case (capitalize first letter)
    formatted_fname = fname.title()

    # Convert last name to title case
    formatted_lname = lname.title()

    # Return full name using formatted string
    return f"{formatted_fname} {formatted_lname}"


# Calling the function and printing the result
print(full_name("John", "Doe"))