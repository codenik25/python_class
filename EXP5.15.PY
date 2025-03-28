# Creating a dictionary
student = {"name": "Alice", "age": 21, "course": "Python"}

# Accessing values
print("Name:", student["name"])

# Adding a new key-value pair
student["grade"] = "A"

# Updating a value
student["age"] = 22

# Removing a key
del student["course"]

# Iterating through a dictionary
for key, value in student.items():
    print(f"{key}: {value}")

# Checking if a key exists
print("Is 'age' in dictionary?", "age" in student)
