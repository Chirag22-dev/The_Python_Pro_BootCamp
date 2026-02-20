# Loop from 1 to 10 (11 is excluded)
for num in range(1, 11):
    print(num)


# Loop from 1 to 10, increasing by 2 (prints only odd numbers)
for num in range(1, 11, 2):
    print(num)


# -----------------------------
# Gauss Challenge
# Calculate the sum of numbers from 1 to 100
# -----------------------------

# Variable to store the total sum
total = 0

# Loop from 1 to 100 (101 is excluded)
for num in range(1, 101):
    total += num

# Print the final sum
print(total)
