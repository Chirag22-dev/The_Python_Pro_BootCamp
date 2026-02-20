# Import the random module to generate random numbers
import random

# Generate a random integer between 1 and 10 (both included)
random_integer = random.randint(1, 10)
print(random_integer)

# Generate a random floating-point number between 0.0 and 1.0
random_number_0_to_1 = random.random()
print(random_number_0_to_1)

# Generate a random floating-point number between 1 and 10
random_float = random.uniform(1, 10)
print(random_float)

# Generate either 0 or 1 randomly (used for coin toss)
head_or_tail = random.randint(0, 1)

# Check the value and print the result of the coin toss
if head_or_tail == 0:
    print("Head")
else:
    print("Tail")
