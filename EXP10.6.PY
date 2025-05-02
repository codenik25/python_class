import re

text = input("Enter a string: ")
pattern = r'^\w+'

match = re.match(pattern, text)
if match:
    print("Word at beginning:", match.group())
else:
    print("No word found at beginning.")
