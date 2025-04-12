from grade_manager import add_student, add_assignment, record_grade, display_grades, display_student_grades

if __name__ == "__main__":
    while True:
        print("\nGrade Tracker Menu:")
        print("1. Add Student")
        print("2. Add Assignment")
        print("3. Record Grade")
        print("4. Display All Grades")
        print("5. Display Student Grades")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            student_name = input("Enter student name: ")
            add_student(student_name)
        elif choice == '2':
            assignment_name = input("Enter assignment name: ")
            add_assignment(assignment_name)
        elif choice == '3':
            student_name = input("Enter student name: ")
            assignment_name = input("Enter assignment name: ")
            grade = input("Enter grade: ")
            record_grade(student_name, assignment_name, grade)
        elif choice == '4':
            display_grades()
        elif choice == '5':
            student_name = input("Enter student name: ")
            display_student_grades(student_name)
        elif choice == '6':
            print("Exiting Grade Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")