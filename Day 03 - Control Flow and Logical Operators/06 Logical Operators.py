# Take user inputs
age = int(input("Enter your age: "))
has_id = input("Do you have an ID card? (Y/N): ")
has_vip = input("Do you have a VIP pass? (Y/N): ")
is_banned = input("Are you banned? (Y/N): ")

# Check eligibility using and, or, not
if (age >= 18 and has_id == "Y") or has_vip == "Y" and not is_banned == "Y":
    print("You are allowed to watch the movie.")
else:
    print("Sorry, you are not allowed to watch the movie.")
