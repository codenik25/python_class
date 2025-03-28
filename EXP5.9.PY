nums = []
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    nums.append(num)

nums.sort()
print("Sorted values:")
for num in nums:
    print(num)
