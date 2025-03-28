# Program to turn every item of a list into its square

# Get user input and split it into a list
user_input = input("Enter elements separated by space: ").split()

# Convert input to integers
numbers = [int(num) for num in user_input]

# Squaring each element
squared_numbers = [num ** 2 for num in numbers]

# Printing result
print("List after squaring each element:", squared_numbers)

