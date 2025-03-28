# Python program to count vowels in a word

# Taking input from the user
word = input("Enter a word: ").lower()  # Convert input to lowercase for case insensitivity

# Defining vowels
vowels = "aeiou"

# Counting vowels
vowel_count = 0
for char in word:
    if char in vowels:
        vowel_count += 1

# Displaying the result
print("Number of vowels in the word:", vowel_count)
