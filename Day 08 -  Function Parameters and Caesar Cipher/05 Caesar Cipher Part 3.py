# List of lowercase alphabets used for Caesar cipher shifting
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
 'u', 'v', 'w', 'x', 'y', 'z']


# Function definition
# Performs Caesar cipher encryption or decryption based on direction
def caesar(original_text, shift_amount, direction):

    # Variable to store the final output text
    output_text = ""

    # If direction is decode, reverse the shift direction
    if direction == "decode":
        shift_amount *= -1

    # Loop through each letter in the input text
    for letter in original_text:
        # Find the index of the letter and apply the shift
        shifted_position = alphabets.index(letter) + shift_amount

        # Use modulo to wrap around the alphabet list
        shifted_position %= 26

        # Append the shifted letter to the output text
        output_text += alphabets[shifted_position]

    # Print the final result after processing all letters
    print(f"Your encrypted message is {output_text}.")


# Control variable for the program loop
should_continue = True

# Loop keeps running until the user decides to stop
while should_continue:

        # Ask the user whether to encode or decode
        choose = input("Type 'encode' for encrypt or 'decode' for decrypt: \n").lower()

        # Take the message input from the user and convert it to lowercase
        text = str(input("Type your message: \n")).lower()

        # Take the shift number for the Caesar cipher
        shift = int(input("Type the shift number: \n"))

        # Call the caesar function with user inputs
        caesar(original_text=text, shift_amount=shift, direction=choose)

        # Ask the user if they want to continue
        restart = input("Do you want to continue 'yes' or 'no': \n").lower()

        # Stop the loop if the user chooses not to continue
        if restart == "no":
            should_continue = False
