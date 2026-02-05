# List of lowercase alphabets used for indexing
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
 'u', 'v', 'w', 'x', 'y', 'z']

# Ask user whether to encode or decode (input is taken but not used yet)
choose = input("Type 'encode' for encrypt or 'decode' for decrypt: \n").lower()

# Take the message input and convert it to lowercase
text = str(input("Type your message: \n")).lower()

# Take the shift value for decryption
shift = int(input("Type the shift number: \n"))


# Function definition
# Decrypts the given text by shifting letters backwards
def decrypt(original_text, shift_amount):

    # Variable to store the decrypted result
    decrypted_text = ""

    # Loop through each character in the original text
    for letter in original_text:

        # Find the letter position and subtract the shift amount
        shifted_position = alphabets.index(letter) - shift_amount

        # Use modulo to wrap around the alphabet list
        shifted_position %= 26

        # Append the decrypted letter to the result string
        decrypted_text += alphabets[shifted_position]

        # This print statement runs INSIDE the loop
        # So it prints the message character-by-character
        print(f"Your decrypted message is {decrypted_text}.")


# Function call
# Calls the decrypt function with user-provided text and shift value
decrypt(original_text=text, shift_amount=shift)
