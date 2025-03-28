nums = []
while True:
    try:
        num = input("Enter a number (blank to stop): ")
        if num == "":
            break
        nums.append(int(num))
    except ValueError:
        print("Please enter a valid integer.")

negatives = [x for x in nums if x < 0]
zeros = [x for x in nums if x == 0]
positives = [x for x in nums if x > 0]

sorted_nums = negatives + zeros + positives

print("Sorted numbers by sign:")
print(*sorted_nums, sep=", ")
