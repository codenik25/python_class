# Program to find even numbers from a list

# Get user input and split it into a list
user_input = input("Enter elements separated by space: ").split()

# Convert input to integers
numbers = [int(num) for num in user_input]

# Filtering even numbers
evens = [num for num in numbers if num % 2 == 0]

# Printing result
print("Even numbers:", evens)
