# Program to count letters, digits, and special symbols in a string

# Taking input from the user
my_string = input("Enter a string: ")

# Initializing counters
letter_count = 0
digit_count = 0
special_count = 0

# Iterating through each character in the string
for char in my_string:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1
    else:
        special_count += 1

# Printing the counts
print("Letters:", letter_count)
print("Digits:", digit_count)
print("Special symbols:", special_count)
