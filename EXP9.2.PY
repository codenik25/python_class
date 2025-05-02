try:
    items = [10, 20, 30]
    index = int(input("Enter index to access (0-2): "))
    print("Item at index", index, "is", items[index])
except IndexError:
    print("Error: Index out of range!")
