# Print a welcome message for the user
print("Welcome to the rollercoaster!")

# Ask the user to enter their height in centimeters
# input() returns a string, so we convert it to an integer using int()
height = int(input("Please enter your height in centimeters: "))

# Check if the user's height is 120 cm or more
if height >= 120:
    # If condition is true, allow the user to ride
    print("You can ride the rollercoaster!")
else:
    # If condition is false, deny the ride
    print("Sorry you have to grow taller to ride the rollercoaster!")
