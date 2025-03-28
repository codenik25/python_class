def max_min_k_elements(tup, k):
    sorted_tup = sorted(tup)
    return sorted_tup[:k], sorted_tup[-k:]

tup = (7, 2, 9, 1, 5, 8, 3, 6)
k = 2
min_k, max_k = max_min_k_elements(tup, k)

print(f"Minimum {k} elements:", min_k)
print(f"Maximum {k} elements:", max_k)
