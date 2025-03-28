def find_min_max_positions(lst):
    min_pos = lst.index(min(lst))
    max_pos = lst.index(max(lst))
    return min_pos, max_pos

lst = [10, 2, 30, 4, 50, 1]
min_pos, max_pos = find_min_max_positions(lst)

print(f"Minimum value position: {min_pos}")
print(f"Maximum value position: {max_pos}")
