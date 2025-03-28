def replace_value(lst, old, new):
    return [new if item == old else item for item in lst]

lst = [1, 2, 3, 4, 2, 5]
old_value = int(input("Enter the value to replace: "))
new_value = int(input("Enter the new value: "))

print("Updated List:", replace_value(lst, old_value, new_value))
