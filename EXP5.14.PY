def create_tuple_list(lst):
    return [(num, num ** 3) for num in lst]

lst = [1, 2, 3, 4, 5]
print("List of tuples (number, cube):", create_tuple_list(lst))
