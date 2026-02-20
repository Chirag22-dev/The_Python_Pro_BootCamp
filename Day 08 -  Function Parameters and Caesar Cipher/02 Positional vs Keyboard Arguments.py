# Function definition
# Takes two parameters: name and location
def greet_with(name, locn):
    # Prints a greeting message using both parameters
    print(f"Hello {name}, from {locn}")

# Positional arguments
# Values are passed based on the order of parameters
greet_with("Chirag", "Bengaluru")

# Keyword arguments
# Values are passed by explicitly specifying parameter names
greet_with(name="Chirag", locn="Bengaluru")
