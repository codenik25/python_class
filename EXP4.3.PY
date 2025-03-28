# Program to check if a string is a palindrome

# Taking input from the user
my_string = input("Enter a string: ")

# Converting to lowercase to make it case-insensitive
my_string = my_string.lower()

# Checking if the string is equal to its reverse
if my_string == my_string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
