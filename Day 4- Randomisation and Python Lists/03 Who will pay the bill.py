# Import the random module to work with random selections
import random

# Create a list of friends' names
friends = ["Chirag", "Sajin", "Ratan", "Poorna"]

# Method 1: Randomly select one element directly from the list
choice_1 = random.choice(friends)
print(choice_1)

# Method 2: Generate a random index number between 0 and 3
choice_2 = random.randint(0, 3)

# Use the random index to select a friend from the list
print(friends[choice_2])
