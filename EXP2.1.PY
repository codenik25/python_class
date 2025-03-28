#Write a program to check whether an entered year is leap or not.
year=int(input("Enter the year:"))
if(year%4==0):
    print(year,"is a leap year")
elif(year!=0): 
    print(year,"is not a leap year")