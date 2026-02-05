# Function definition
# Calculates a love score based on occurrences of letters in two names
def calculate_love_score(name_1, name_2):

    # Combine both names and convert to lowercase for consistent counting
    combine_names = (name_1 + name_2).lower()

    # Variable to store count of letters from the word "true"
    true_count = 0
    for letter in "true":
        # Count how many times each letter appears and add to total
        true_count += combine_names.count(letter)

    # Variable to store count of letters from the word "love"
    love_count = 0
    for letter in "love":
        # Count how many times each letter appears and add to total
        love_count += combine_names.count(letter)

    # Combine both counts to form the love score
    love_score = str(true_count) + str(love_count)

    # Display the final love score
    print(f"Your score is {love_score}")

# Function calls with different name combinations
calculate_love_score("Srikanth Sharma", "Aihika Sharma")
calculate_love_score("Srikanth Sharma", "Aishwarya Sharma")
