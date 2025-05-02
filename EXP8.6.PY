#m57. Write a Program to illustrate multilevel inheritance in Python

class Grandparent:
    def show_gp(self):
        print("Grandparent traits")

class Parent(Grandparent):
    def show_parent(self):
        print("Parent traits")

class Child(Parent):
    def show_child(self):
        print("Child traits")

c = Child()
c.show_gp()
c.show_parent()
c.show_child()
