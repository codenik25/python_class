import random

def password():
    n=random.randint(7,10)
    print(n)

    p=''
    for i in range(n):
        p+=chr(random.randint(33,126))
    return p
print(password())