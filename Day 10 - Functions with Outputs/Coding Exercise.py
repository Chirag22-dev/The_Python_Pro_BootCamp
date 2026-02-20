# Function to check whether a given year is a leap year
def is_leap_year(year):

    # A year is a leap year if:
    # 1. It is divisible by 4 AND not divisible by 100
    # OR
    # 2. It is divisible by 400
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


# Test cases
print(is_leap_year(2400))  # Expected: True (divisible by 400)
print(is_leap_year(1989))  # Expected: False (not divisible by 4)