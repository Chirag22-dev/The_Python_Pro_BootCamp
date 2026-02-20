"""
The Body Mass Index (BMI) is used to check whether a person
is underweight, normal weight, or overweight.

Formula:
BMI = weight / (height ** 2)
"""

# Height of the person (units should be consistent, usually meters)
height = 45

# Weight of the person (usually in kilograms)
weight = 80

# Calculate BMI using the formula
# ** has higher priority, so height ** 2 is calculated first
bmi = weight / height ** 2

# Print the calculated BMI
print(bmi)
