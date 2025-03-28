def swapping(a,b):
    a,b=b,a
    return a,b

a=input("Enter the value of a:")
b=input("Enter the value of b:")
print("Before swapping the value would be ",a,'and',b)
a,b=swapping(a,b)
print("After swapping the value would be ",a,'and',b)