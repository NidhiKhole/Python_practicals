# Student Result using Different Types of Arguments


# Positional Arguments
def student_result(name, marks1, marks2, marks3):
    total = marks1 + marks2 + marks3
    percentage = total / 3
    print("\nStudent Name:", name)
    print("Total Marks:", total)
    print("Percentage:", percentage)
    return percentage


# Keyword Arguments
def display_student(name, course):
    print("\nName:", name)
    print("Course:", course)


# Default Argument
def calculate_grade(percentage, passing_marks=40):
    if percentage >= 75:
        return "Distinction"
    elif percentage >= 60:
        return "First Class"
    elif percentage >= passing_marks:
        return "Pass"
    else:
        return "Fail"


# Variable-Length Arguments
def calculate_total(*marks):
    total = 0
    for mark in marks:
        total += mark
    return total


# Main Program
name = input("Enter student name: ")
m1 = float(input("Enter marks in Subject 1: "))
m2 = float(input("Enter marks in Subject 2: "))
m3 = float(input("Enter marks in Subject 3: "))

# Positional arguments
percentage = student_result(name, m1, m2, m3)

# Keyword arguments
display_student(name=name, course="B.Tech AI & ML")

# Variable-length arguments
total = calculate_total(m1, m2, m3)
print("Total using *args:", total)

# Default argument
grade = calculate_grade(percentage)
print("Grade:", grade)