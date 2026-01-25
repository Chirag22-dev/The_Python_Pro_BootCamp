"""
Program: FizzBuzz Game
Rules:
- Print numbers from 1 to 100
- If a number is divisible by 3, print "Fizz"
- If a number is divisible by 5, print "Buzz"
- If a number is divisible by both 3 and 5, print "FizzBuzz"
"""

# Loop through numbers from 1 to 100 (inclusive)
for num in range(1, 101):

    # Check if number is divisible by both 3 and 5 first
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")

    # Check if number is divisible by 3
    elif num % 3 == 0:
        print("Fizz")

    # Check if number is divisible by 5
    elif num % 5 == 0:
        print("Buzz")

    # If none of the above conditions match, print the number
    else:
        print(num)
