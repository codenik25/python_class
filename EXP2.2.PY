# Python program to find the largest among three numbers

# Taking input from the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

# Using nested if-else to find the largest number
if a > b:
    if a > c:
        print(a, "is larger than",b,"and",c)
    else:
        print(c, "is larger than",a,"and",b)
elif b > c:
    print(b, "is larger than",a,"and",c)
else:
    print(c, "is larger than",a,"and",b)
