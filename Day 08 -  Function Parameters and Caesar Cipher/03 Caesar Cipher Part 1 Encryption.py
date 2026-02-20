# List containing all lowercase alphabets
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
 'u', 'v', 'w', 'x', 'y', 'z']

# Ask the user whether to encode or decode
choose = input("Type 'encode' for encrypt or 'decode' for decrypt: \n").lower()

# Take the message input from the user and convert it to lowercase
text = str(input("Type your message: \n")).lower()

# Take the shift number for encryption
shift = int(input("Type the shift number: \n"))

# Function definition
# Encrypts the given text using a shift value
def encrypt(original_text, shift_amount):

    # Variable to store the encrypted result
    encrypted_text = ""

    # Loop through each character in the original text
    for letter in original_text:
        # Find the index of the letter and apply the shift
        shifted_position = alphabets.index(letter) + shift_amount

        # Use modulo to wrap around if index exceeds alphabet length
        shifted_position %= 26

        # Add the shifted letter to the encrypted text
        encrypted_text += alphabets[shifted_position]

    # Print the final encrypted message
    print(f"Your encrypted message is {encrypted_text}.")

# Function call
# Passes user input text and shift value to the encrypt function
encrypt(original_text=text, shift_amount=shift)
