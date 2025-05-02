# 59. Write a Program to illustrate hybrid inheritance in Python

class School:
    def show_school(self):
        print("School class")

class Student(School):
    def show_student(self):
        print("Student class")

class Teacher(School):
    def show_teacher(self):
        print("Teacher class")

class TA(Student, Teacher):
    def show_ta(self):
        print("Teaching Assistant")

ta = TA()
ta.show_school()
ta.show_student()
ta.show_teacher()
ta.show_ta()
