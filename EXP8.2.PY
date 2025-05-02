# 53. Write a Program to implement Getters and Setters in a class

class Student:
    def __init__(self):
        self._name = ""

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

s = Student()
s.set_name("Nikunj")
print("Student Name:", s.get_name())
