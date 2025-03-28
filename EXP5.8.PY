def cumulative_sum(lst):
    cum_sum = []
    total = 0
    for num in lst:
        total += num
        cum_sum.append(total)
    return cum_sum

lst = [1, 2, 3, 4, 5]
print("Cumulative Sum:", cumulative_sum(lst))
