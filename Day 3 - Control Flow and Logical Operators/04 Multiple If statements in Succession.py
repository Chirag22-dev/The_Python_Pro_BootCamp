# Welcome message
print("Welcome to the rollercoaster!")

# Get user's height in centimeters
height = int(input("Please enter your height in centimeters: "))
bill = 0
# Check height eligibility
if height >= 120:
    print("You can ride the rollercoaster!")

    # Get user's age
    age = int(input("Please enter your age: "))

    # Determine ticket price based on age
    if age < 12:
        bill = 5
        print("Child Tickets are $5.")
    elif age <= 18:
        bill = 8
        print("Youth Tickets are $8.")
    else:
        bill = 12
        print("Please pay $12.")

    wants_pic = input("Would you like to see a picture? y/n: ")
    if wants_pic == "y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry you have to grow taller to ride the rollercoaster!")
