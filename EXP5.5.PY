# Program to check if all elements in a list are unique

# Get user input and split it into a list
user_input = input("Enter elements separated by space: ").split()

# Convert input to integers
numbers = [int(num) for num in user_input]

# Check uniqueness using set
is_unique = len(numbers) == len(set(numbers))

# Printing result
print("All elements are unique:" if is_unique else "There are duplicate elements.")
