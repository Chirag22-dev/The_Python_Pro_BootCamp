# Importing the logo variable from the logo file
from logo import logo

# Printing the logo on the screen
print(logo)

# Empty dictionary to store auction data (name : bid amount)
auction_data = {}


# Function to find the highest bidder
def bidding_comparison(bidding_dictionary):
    # Variable to store the winner's name
    winner = ""

    # Variable to store the highest bid amount
    highest_bid = 0

    # Loop through each bidder in the dictionary
    for bidder in bidding_dictionary:

        # Get the bid amount for the current bidder
        bid_amount = bidding_dictionary[bidder]

        # Check if the current bid is higher than the highest bid
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    # Print the winner and the highest bid
    print(f"The winner is {winner} with a bid of ${highest_bid}")


# Variable to control the auction loop
should_continue = True

# Loop to keep accepting bids until no more bidders
while should_continue:

    # Taking bidder's name as input
    name = str(input("Enter your name: "))

    # Taking bidder's bid price as input
    bid_price = float(input("Enter bid price: "))

    # Storing name and bid price in the auction dictionary
    auction_data[name] = bid_price

    # Asking if there are more bidders
    available_bidders = str(
        input("If there are any other bidders. yes or no: ")
    ).lower()

    # If there are more bidders, continue the loop
    if available_bidders == "yes":
        should_continue = True

        # Clearing the screen by printing blank lines
        print("\n" * 50)

    # If no more bidders, stop the loop and find the winner
    elif available_bidders == "no":
        should_continue = False
        bidding_comparison(auction_data)
