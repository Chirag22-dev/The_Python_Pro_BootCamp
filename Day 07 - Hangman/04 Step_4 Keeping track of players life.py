import random
# Importing the random module to choose a random word

word_list = ["lion", "tiger", "cheetah", "koala"]
# List of possible words for the game
lives = 6
hangman_stages = [
    """
     ------
     |    |
     O    |
    /|\\   |
    / \\   |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
    /     |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
          |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
    /|    |
          |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
     |    |
          |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
          |
          |
          |
    =========
    """,
    """
     ------
     |    |
          |
          |
          |
          |
    =========
    """
]

chosen_word = random.choice(word_list)
# Randomly selects one word from the list

print(chosen_word)
# Prints the chosen word (useful for testing/debugging)

place_holder = ""
# Empty string to store underscores representing hidden letters

length = len(chosen_word)
# Finds the length of the chosen word

for i in range(length):
    # Loop runs once for each letter in the chosen word
    place_holder += "_"
    # Adds an underscore for each letter

print(place_holder)
# Displays the initial hidden word (e.g. "_____")

game_over = False
# Controls the game loop

correct_word = []
# List to store correctly guessed letters

while not game_over:
    # Loop continues until the user wins the game

    guess = input("Guess a letter: ")
    # Takes a letter guess from the user

    display = ""
    # Empty string to build the word display after each guess

    for letter in chosen_word:
        # Loop through each letter in the chosen word

        if letter == guess:
            # If guessed letter matches the current letter
            display += letter
            # Add the guessed letter to display
            correct_word.append(guess)
            # Store the correct guess

        elif letter in correct_word:
            # If the letter was guessed correctly earlier
            display += letter
            # Reveal the letter

        else:
            # If the letter has not been guessed yet
            display += "_"
            # Keep it hidden

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose!")



    if display == chosen_word:
        # Checks if the entire word has been guessed
        game_over = True
        # Ends the game loop
        print("You Win!")
        # Displays winning message

    print(display)
    # Shows the current state of the guessed word
    print(hangman_stages[lives])