# Program to interchange first and last element of a list

# Get user input and split it into a list
user_input = input("Enter elements separated by space: ").split()

# Convert input to integers
numbers = [int(num) for num in user_input]

# Swapping first and last element if list is not empty
if len(numbers) > 1:
    numbers[0], numbers[-1] = numbers[-1], numbers[0]

# Printing result
print("List after swapping first and last element:", numbers)
