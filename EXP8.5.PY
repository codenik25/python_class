# 56. Write a Program to illustrate multiple inheritance in Python

class Father:
    def show_father(self):
        print("Father's traits")

class Mother:
    def show_mother(self):
        print("Mother's traits")

class Child(Father, Mother):
    pass

c = Child()
c.show_father()
c.show_mother()
