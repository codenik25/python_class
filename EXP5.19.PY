def are_anagrams(word1, word2):
    return sorted(word1.lower()) == sorted(word2.lower())

word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

if are_anagrams(word1, word2):
    print("The words are anagrams.")
else:
    print("The words are not anagrams.")
