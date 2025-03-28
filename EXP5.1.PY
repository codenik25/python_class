# List Operations Demonstration in Python

# Creating a list
my_list = [10, 20, 30, 40, 50]
print("Original List:", my_list)

# Adding elements
my_list.append(60)
print("After Append:", my_list)

my_list.insert(2, 25)  # Inserting at index 2
print("After Insert at index 2:", my_list)

# Removing elements
my_list.remove(30)  # Removes first occurrence of 30
print("After Removing 30:", my_list)

popped_element = my_list.pop()  # Removes last element
print("After Pop (removing last element):", my_list, "(Popped Element:", popped_element, ")")

# List slicing
sub_list = my_list[1:4]  # Extracting a sublist
print("Sliced List (index 1 to 3):", sub_list)

# Sorting list
my_list.sort()
print("Sorted List:", my_list)

my_list.reverse()
print("Reversed List:", my_list)

# Iterating through a list
print("Iterating through list:")
for item in my_list:
    print(item, end=' ')
print()
