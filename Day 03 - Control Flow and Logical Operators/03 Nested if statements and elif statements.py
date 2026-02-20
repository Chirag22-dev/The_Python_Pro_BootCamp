# Welcome message
print("Welcome to the rollercoaster!")

# Get user's height in centimeters
height = int(input("Please enter your height in centimeters: "))

# Check height eligibility
if height >= 120:
    print("You can ride the rollercoaster!")

    # Get user's age
    age = int(input("Please enter your age: "))

    # Determine ticket price based on age
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $8.")
    else:
        print("Please pay $12.")
else:
    print("Sorry you have to grow taller to ride the rollercoaster!")
