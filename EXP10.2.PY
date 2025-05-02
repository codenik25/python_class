import re

text = input("Enter a string: ")
pattern = r'^[A-Z]\w+$'

if re.fullmatch(pattern, text):
    print("Match found.")
else:
    print("No match.")
