import re

text = input("Enter a string: ")
pattern = r'^\w+$'

if re.match(pattern, text):
    print("Valid string: contains only letters, digits, and underscores.")
else:
    print("Invalid string.")
