# List containing student scores
student_score = [12, 23, 45, 67, 87, 54]

# Variable to store the total sum of scores
total = 0

# Loop through each score and add it to total
for score in student_score:
    total += score

# Print the final sum of all scores
print(total)


# Variable to store the maximum score
max_score = 0

# Loop through each score to find the highest value
for score in student_score:
    if score > max_score:
        max_score = score

# Print the maximum score
print(max_score)
