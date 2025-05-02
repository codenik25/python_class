'''Write a program that reads values from the user until a blank line is
entered. Display the total of all of the values entered by the user (or 0.0
if the first value entered is a blank line). Complete this task using
recursion. Your program may not use any loops.'''

def recursive_sum():
    val = input("Enter a number (blank to stop): ")
    if val == "":
        return 0.0
    return float(val) + recursive_sum()

total = recursive_sum()
print("Total sum:", total)
