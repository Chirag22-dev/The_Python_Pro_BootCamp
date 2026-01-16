# Display a welcome message
print("Welcome to Tip Calculator")

# Take the total bill amount from the user and convert it to float
bill = float(input("What was the total bill? $"))

# Take tip percentage from the user and convert it to integer
tip = int(input("What was the percentage tip? "))

# Take number of people to split the bill
split = int(input("How many splits? "))

# Convert tip percentage into decimal value
tip_percent = tip / 100

# Calculate the total tip amount
total_tip_amount = bill * tip_percent

# Calculate the total bill including tip
total_bill = bill + total_tip_amount

# Split the total bill among the given number of people
bill_with_split = total_bill / split

# Round the final amount to 2 decimal places
final_bill = round(bill_with_split, 2)

# Display the final bill and per-person amount
print(f"Your final bill is ${total_bill} and each person should pay ${final_bill}")
