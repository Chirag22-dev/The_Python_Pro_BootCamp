# Welcome message for the user
print("Welcome to Python Pizza Deliveries")

# Taking user inputs for pizza options
size = input("Please enter the size of the pizza S, M, L: ")
pepperoni = input("Please enter the pepperoni on the pizza Y or N: ")
extra_cheese = input("Please enter the extra cheese on the pizza Y or N: ")

# Initialize the total bill amount
bill = 0

# Add cost based on pizza size
if size == "S":
    bill += 10
elif size == "M":
    bill += 15
elif size == "L":
    bill += 20
else:
    # Handles invalid size input
    print("Sorry you have to enter S, M, or L")

# Add cost for pepperoni
if pepperoni == "Y":
    if size == "S":
        bill += 2  # Extra cost for small pizza pepperoni
    else:
        bill += 3  # Extra cost for medium or large pizza pepperoni

# Add cost for extra cheese
if extra_cheese == "Y":
    bill += 1

# Display the final bill to the user
print(f"Your total bill is ${bill}")
