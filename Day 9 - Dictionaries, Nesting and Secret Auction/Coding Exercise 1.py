# Dictionary storing students' names as keys and their scores as values
student_scores = {
    "Chirag": 99,
    "Dhanush": 98,
    "Dhanush M": 69,
    "Dheva C": 88,
    "Gagan": 74,
    "Shreyas": 50
}

# Empty dictionary to store final grades of students
student_grades = {}

# Looping through each student in the student_scores dictionary
for student in student_scores:

    # Getting the score of the current student
    score = student_scores[student]

    # Assigning grade based on the score
    if score >= 90:
        grade = "Outstanding"

    elif score >= 80:
        grade = "Excellant"

    elif score >= 70:
        grade = "Fair"

    elif score >= 60:
        grade = "Poor"

    else:
        grade = "Fail"

    # Storing the student's grade in the student_grades dictionary
    student_grades[student] = grade

# Printing the final dictionary with students and their grades
print(student_grades)
