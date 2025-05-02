# 58. Write a Program to illustrate heirarchical inheritance in Python

class Parent:
    def show_parent(self):
        print("Parent class")

class Child1(Parent):
    def show_child1(self):
        print("Child 1 class")

class Child2(Parent):
    def show_child2(self):
        print("Child 2 class")

c1 = Child1()
c2 = Child2()
c1.show_parent()
c1.show_child1()
c2.show_parent()
c2.show_child2()
