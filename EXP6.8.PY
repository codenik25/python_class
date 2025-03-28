smallest = lambda a, b: a if a < b else b

# Taking input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Smallest number is:", smallest(num1, num2))
