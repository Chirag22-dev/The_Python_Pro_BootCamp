import random  # Import random module to generate computer's choice

# ASCII art for Rock
rock = '''
🪨 ROCK
      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
'''

# ASCII art for Paper
paper = '''
📄 PAPER
       _______
  ---'    ____)____
             ______)
            _______)
           _______)
  ---.__________)
'''

# ASCII art for Scissors
scissors = '''
✂️ SCISSORS
      _______
  ---'   ____)____
            ______)
         __________)
        (____)
  ---.__(___)
'''

# Welcome message
print("Welcome to the Rock Paper Scissors game!")

"""
Game Rules:
Rock beats scissors
Paper beats rock
Scissors beats paper
"""

# Store all game images in a list for easy access using index
images = [rock, paper, scissors]

# Take user input
user_choice = int(input("Type 0 for Rock, 1 for Paper, 2 for Scissors: "))

# If user input is valid, display user's choice
if user_choice >= 0 and user_choice <= 2:
    print("You chose:")
    print(images[user_choice])

# Generate computer's random choice (0, 1, or 2)
computer_choice = random.randint(0, 2)

# Display computer's choice
print("Computer choice:")
print(images[computer_choice])

# Check for invalid input
if user_choice >= 3 or user_choice < 0:
    print("❌ You typed an invalid value. You lose!")

# Winning conditions
elif user_choice == 0 and computer_choice == 2:
    print("🎉 You win!")

elif user_choice == 1 and computer_choice == 0:
    print("🎉 You win!")

elif user_choice == 2 and computer_choice == 1:
    print("🎉 You win!")

# Losing conditions
elif user_choice == 2 and computer_choice == 0:
    print("😢 You lose!")

elif user_choice == 0 and computer_choice == 1:
    print("😢 You lose!")

elif user_choice == 1 and computer_choice == 2:
    print("😢 You lose!")

# Draw condition
elif user_choice == computer_choice:
    print("🤝 It's a draw!")
