n = int(input("Enter the number of terms: "))

a, b = 0, 1  # First two terms of Fibonacci series

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b  # Update values for next term
