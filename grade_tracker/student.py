class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, assignment, grade):
        self.grades[assignment] = grade

    def get_grade(self, assignment):
        return self.grades.get(assignment, None)

    def calculate_average(self):
        valid_grades = [grade for grade in self.grades.values() if grade is not None]
        if valid_grades:
            return sum(valid_grades) / len(valid_grades)
        return 0

    def __str__(self):
        return self.name