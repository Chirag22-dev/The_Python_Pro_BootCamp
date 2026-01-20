# Print the ASCII art title of the game
print('''
 ______  ____     ___   ____  _____ __ __  ____     ___      __ __  __ __  ____   ______
|      ||    \   /  _] /    |/ ___/|  |  ||    \   /  _]    |  |  ||  |  ||    \ |      |
|      ||  D  ) /  [_ |  o  (   \_ |  |  ||  D  ) /  [_     |  |  ||  |  ||  _  ||      |
|_|  |_||    / |    _]|     |\__  ||  |  ||    / |    _]    |  _  ||  |  ||  |  ||_|  |_|
  |  |  |    \ |   [_ |  _  |/  \ ||  :  ||    \ |   [_     |  |  ||  :  ||  |  |  |  |
  |  |  |  .  \|     ||  |  |\    ||     ||  .  \|     |    |  |  ||     ||  |  |  |  |
  |__|  |__|\_||_____||__|__| \___| \__,_||__|\_||_____|    |__|__| \__,_||__|__|  |__|
''')

# Display the welcome message and game mission
print("Welcome to the Treasure Island.\nYour mission is to find the treasure.")

# Ask the user to choose a direction and convert input to lowercase
side = input("Which side do you want to go? Right or Left? ").lower()

# Check if the user chose the left path
if side == "left":

    # Ask the user what activity they want to do
    activity = input("Which activity do you want to do? Swim or Wait? ").lower()

    # If the user chooses to swim
    if activity == "swim":
        print("Attacked by trout.\nGame Over")

    # If the user chooses to wait
    elif activity == "wait":

        # Ask the user to choose a door color
        door = input("Which colour of door do you want to enter? Red, Blue, Yellow? ").lower()

        # Check which door was chosen
        if door == "red":
            print("Burned by fire.\nGame Over")
        elif door == "blue":
            print("Eaten by Beasts.\nGame Over")
        elif door == "yellow":
            print("You Win!")
        else:
            # If the door choice is invalid
            print("Please enter a valid option.")

    else:
        # If the activity choice is invalid
        print("Please enter a valid option.")

# If the user chooses the right path
elif side == "right":
    print("Fall into a hole.\nGame Over.")

# If the side choice is invalid
else:
    print("Please enter a valid option.")
