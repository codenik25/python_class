import re

text = input("Enter a string: ")
no_spaces = re.sub(r'\s+', '', text)
print("String without spaces:", no_spaces)
