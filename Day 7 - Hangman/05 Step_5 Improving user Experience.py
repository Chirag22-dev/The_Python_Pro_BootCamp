import random
# Importing random module to select a random word

import words
# Importing words module which contains the word list

import logo
# Importing logo module which contains hangman logo and stages

lives = 6
# Total number of lives allowed for the player

print(logo.hangman_logo)
# Prints the Hangman game logo

choosen_word = random.choice(words.word_list)
# Randomly selects a word from the word list

print(choosen_word)
# Prints the chosen word (for debugging/testing)

place_holder = ""
# Empty string to hold underscores for the hidden word

length = len(choosen_word)
# Length of the chosen word

for word in range(length):
    # Loop runs once for each letter in the chosen word
    place_holder += "_"
    # Adds an underscore for each letter

print(place_holder)
# Displays the initial placeholder (e.g. "_ _ _ _")

game_over = False
# Flag to control the game loop

correct_word = []
# List to store correctly guessed letters

while not game_over:
    # Game loop continues until win or loss

    guess = input("Guess a letter: ").lower()
    # Takes a letter guess from the user and converts it to lowercase

    display = ""
    # Empty string to build the displayed word

    for letter in choosen_word:
        # Loop through each letter in the chosen word

        if letter == guess:
            # If the guessed letter matches the current letter
            display += letter
            # Reveal the letter
            correct_word.append(letter)
            # Store the correct guessed letter

        elif letter in correct_word:
            # If the letter was guessed correctly earlier
            display += letter
            # Reveal the letter

        else:
            # If the letter has not been guessed
            display += "_"
            # Keep it hidden

    if guess in correct_word:
        # Checks if the letter was already guessed before
        print("You have already guessed this letter")
        continue
        # Skip the rest of the loop and ask for a new guess

    if guess not in choosen_word:
        # If the guessed letter is not in the chosen word
        lives -= 1
        # Reduce one life
        print(f"********************************{lives} lives more left************************")

        if lives == 0:
            # If no lives are left
            game_over = True
            # End the game
            print(f"************************It was {choosen_word}. You Lose!**************************")

    if display == choosen_word:
        # Checks if the player has guessed the full word
        game_over = True
        # End the game
        print("******************************You win!*************************************")

    print(logo.hangman_stages[lives])
    # Displays the current hangman stage based on remaining lives

    print(display)
    # Displays the current guessed word
