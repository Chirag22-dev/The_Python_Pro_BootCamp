import random

# Importing the random module to select a random word from the list

word_list = ["lion", "tiger", "cheetah", "koala"]
# List of possible words to choose from

chosen_word = random.choice(word_list)
# Randomly selects one word from the word_list

print(chosen_word)
# Prints the chosen word (useful for testing/debugging)

guess = input("Guess a letter: ").lower()
# Takes a letter input from the user and converts it to lowercase

for letter in chosen_word:
    # Loop through each letter in the chosen word

    if guess == letter:
        # Checks if the guessed letter matches the current letter
        print("Correct")
    else:
        # Executes when the guessed letter does not match
        print("Wrong")
