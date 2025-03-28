# Program to calculate the sum and average of digits in a registration number

# Taking registration number as input
reg_number = input("Enter your registration number: ")

# Extracting digits and calculating sum
digit_sum = sum(int(char) for char in reg_number if char.isdigit())

# Counting the number of digits
digit_count = sum(1 for char in reg_number if char.isdigit())

# Calculating average (handling division by zero)
digit_avg = digit_sum / digit_count if digit_count > 0 else 0

# Printing the results
print("Sum of digits:", digit_sum)
print("Average of digits:", digit_avg)
