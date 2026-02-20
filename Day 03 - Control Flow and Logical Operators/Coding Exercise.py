"""
BMI Categories:
- BMI < 18.5           → underweight
- BMI >= 18.5 and <25  → normal weight
- BMI >= 25            → overweight
"""

# Take user's weight in kilograms
weight = float(input("Please enter your weight in kg: "))

# Take user's height in centimeters
height_cm = float(input("Please enter your height in centimeters: "))

# Convert height from centimeters to meters
height_m = height_cm / 100

# Calculate BMI using the formula
bmi = weight / (height_m ** 2)

# Check BMI category
if bmi < 18.5:
    print("underweight")
elif bmi < 25:   # No need to check bmi >= 18.5 again
    print("normal weight")
else:
    print("overweight")
