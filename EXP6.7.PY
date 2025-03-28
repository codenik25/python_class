user_input = input("Enter elements separated by space: ").split()
a= [int(num) for num in user_input]
x=lambda a:sum(a)
print(x(a))