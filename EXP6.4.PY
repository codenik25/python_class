user_input = input("Enter elements separated by space: ").split()
numbers = [int(num) for num in user_input]
numbers.sort()
print(numbers)
print(numbers[1])