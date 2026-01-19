# Ask the user to enter a number
# input() returns a string, so we convert it to an integer using int()
num = int(input("Please enter a number: "))

# Check if the number is divisible by 2
# If remainder is 0, the number is even
if num % 2 == 0:
    print("Even")
else:
    # If remainder is not 0, the number is odd
    print("Odd")
