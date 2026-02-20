# Function definition
# Well-named function that clearly describes its purpose
def life_in_weeks(age):

    # Clear and readable calculation of remaining years
    years_left = 90 - age

    # Logical conversion from years to weeks using a constant value
    weeks_left = years_left * 52

    # Clean and readable output using an f-string
    print(f"You have {weeks_left} weeks left.")

# Function call
# Simple and direct function invocation with a realistic input value
life_in_weeks(40)
