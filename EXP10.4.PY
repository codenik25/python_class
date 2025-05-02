import re

text = input("Enter a string: ")
pattern = r'ab{3}'

if re.fullmatch(pattern, text):
    print("Match found.")
else:
    print("No match.")
