'''54. Write a Program to calculate student grade using class'''

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        avg = sum(self.marks) / len(self.marks)
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

student = Student("Riya", [85, 78, 92])
print(f"{student.name}'s Grade:", student.calculate_grade())

