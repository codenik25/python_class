import re

text = input("Enter a sentence: ")
patterns = ['apple', 'banana', 'grape']

for word in patterns:
    if re.search(word, text):
        print(f"'{word}' found in the string.")
