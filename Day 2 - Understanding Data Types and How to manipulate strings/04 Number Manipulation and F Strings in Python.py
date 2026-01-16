# A floating-point number
num = 2.34567

# Convert float to integer (decimal part is removed, NOT rounded)
print(int(num))        # Output: 2

# round() without second argument rounds to nearest whole number
print(round(num))      # Output: 2

# round() with second argument rounds to given decimal places
print(round(num, 2))   # Output: 2.35

# -------------------------
# Augmented Assignment
# -------------------------

score = 0

# += means: score = score + 1
score += 1
print(score)           # Output: 1

# -------------------------
# Multiple Data Types
# -------------------------

score = 0              # Integer
height = 1.0           # Float
is_winning = True      # Boolean

# f-string allows inserting variables directly inside the string
print(f"Your score is {score}, your height is {height}. You are winning is {is_winning}")
