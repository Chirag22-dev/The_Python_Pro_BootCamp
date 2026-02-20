import random

# Importing the random module to randomly select a word from the list

word_list = ["lion", "tiger", "cheetah", "koala"]
# List of words from which one word will be chosen

chosen_word = random.choice(word_list)
# Randomly selects one word from word_list

length = len(chosen_word)
# Finds the length of the chosen word

print(chosen_word)
# Prints the chosen word (used for testing/debugging)

placeholder = ""
# Empty string to store underscores representing hidden letters

for i in range(length):
    # Loop runs once for each letter in the chosen word
    placeholder += "_"
    # Adds an underscore for each letter

print(placeholder)
# Displays the placeholder with underscores (e.g. "____")

guess = input("Guess a letter: ").lower()
# Takes a letter input from the user and converts it to lowercase

display = ""
# Empty string to build the displayed word after guessing

for letter in chosen_word:
    # Loop through each letter in the chosen word

    if guess == letter:
        # If guessed letter matches the current letter
        display += letter
        # Add the correct letter to display
    else:
        # If guessed letter does not match
        display += "_"
        # Add underscore instead

print(display)
# Prints the final display showing guessed letters and blanks
