''' 52. Write a Program to implement destructor and constructors using
__del__() and __init__()'''

class Person:
    def __init__(self, name):
        self.name = name
        print(f"Constructor: Hello, {self.name}!")

    def __del__(self):
        print(f"Destructor: Goodbye, {self.name}!")

p = Person("Alice")
del p  # Optional: To force destructor call
