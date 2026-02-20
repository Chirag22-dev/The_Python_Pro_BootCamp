# Addition
print(123 + 45)     # Adds two numbers → Output: 168

# Subtraction
print(21 - 3)       # Subtracts 3 from 21 → Output: 18

# Multiplication
print(12 * 3)       # Multiplies two numbers → Output: 36

# Division (always gives float result)
print(11 / 3)       # Output: 3.6666666666666665

# Modulus (remainder of division)
print(11 % 3)       # 11 divided by 3 leaves remainder → Output: 2

# Floor Division (returns quotient without decimal part)
print(11 // 3)      # Output: 3

# Exponentiation (power)
print(2 ** 3)       # 2 raised to the power 3 → Output: 8

# -------------------------
# PEMDAS Rule (Order of Operations)
# -------------------------
"""
PEMDAS tells Python which operation to perform first:

()   → Parentheses
**   → Exponentiation
* /  → Multiplication or Division
+ -  → Addition or Subtraction
"""

# Expression evaluation using PEMDAS
print(3 * (3 + 3) / 3 - 3)
# Step-by-step:
# (3 + 3) = 6
# 3 * 6 = 18
# 18 / 3 = 6
# 6 - 3 = 3
