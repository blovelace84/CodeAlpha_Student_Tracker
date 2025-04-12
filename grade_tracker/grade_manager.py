import json

grade_file = "student_grades.json"
grades = {}  # Keep the global grades dictionary here if you're not using classes

try:
    with open(grade_file, 'r') as f:
        grades = json.load(f)
    print("Existing grades loaded from file.")
except FileNotFoundError:
    print("No existing grades file found. Starting with an empty tracker.")
except json.JSONDecodeError:
    print("Error decoding JSON from file. Starting with an empty tracker.")

def _save_grades():
    with open(grade_file, 'w') as f:
        json.dump(grades, f, indent=4) #Use index for better readability
    print(f"Grades saved to '{grade_file}'.")

def add_student(student_name):
    global grades
    if student_name not in grades:
        grades[student_name] = {}
        _save_grades() # Save after adding a student
        print(f"Student '{student_name}' added successfully.")
    else:
        print(f"Student '{student_name}' already exists.")

def add_assignment(assignment_name):
    global grades
    for student in grades:
        grades[student][assignment_name] = None
    _save_grades()
    print(f"Assignment '{assignment_name}' added for all students.")

def record_grade(student_name, assignment_name, grade):
    global grades
    if student_name in grades:
        if assignment_name in grades[student_name]:
            try:
                grade = float(grade)
                if 0 <= grade <= 100:
                    grades[student_name][assignment_name] = grade
                    _save_grades()
                    print(f"Grade {grade} recorded for '{student_name}' in '{assignment_name}'.")
                else:
                    print("Invalid grade. Please enter a value between 0 and 100.")
            except ValueError:
                print("Invalid grade format. Please enter a number.")
        else:
            print(f"Assignment '{assignment_name}' not found for '{student_name}'.")
    else:
        print(f"Student '{student_name}' not found.")

def calculate_average(student_name):
    global grades
    if student_name in grades:
        student_grades = [grade for grade in grades[student_name].values() if grade is not None]
        if student_grades:
            average = sum(student_grades) / len(student_grades)
            return average
        else:
            return 0
    else:
        print(f"Student '{student_name}' not found.")
        return None

def display_grades():
    global grades
    print("\n--- Student Grades ---")
    if not grades:
        print("No students or grades recorded yet.")
        return
    for student, assignments in grades.items():
        print(f"\n{student}:")
        if assignments:
            for assignment, grade in assignments.items():
                print(f"  {assignment}: {grade if grade is not None else 'Not Graded'}")
            average = calculate_average(student)
            print(f"  Average: {average:.2f}")
        else:
            print("  No grades recorded for this student.")
    print("----------------------\n")

def display_student_grades(student_name):
    global grades
    if student_name in grades:
        print(f"\n--- Grades for {student_name} ---")
        if grades[student_name]:
            for assignment, grade in grades[student_name].items():
                print(f"  {assignment}: {grade if grade is not None else 'Not Graded'}")
            average = calculate_average(student_name)
            print(f"  Average: {average:.2f}")
        else:
            print("  No grades recorded for this student.")
        print("---------------------------\n")
    else:
        print(f"Student '{student_name}' not found.")