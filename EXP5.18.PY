def unique_char_count(string):
    char_dict = {}
    for char in string:
        if char.isalnum():  # Only consider alphanumeric characters
            char_dict[char] = char_dict.get(char, 0) + 1
    return len(char_dict)

user_input = input("Enter a string: ")
print(f"Number of unique characters: {unique_char_count(user_input)}")
