def disc(a,b,c):
    return (b**2) - (4*a*c)

def root(a):
    return a ** 0.5 

def pos(a,b,c):
    return -b + root(disc(a,b,c))

def neg(a,b,c):
    return -b - root(disc(a,b,c))

def proot(a,b,c):
    return pos(a,b,c) / (2*a)

def nroot(a,b,c):
    return neg(a,b,c) / (2*a)

d = ""

print("ax^2 + bx + c \n"
"Please input the coefficients")

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

p = proot(a,b,c)
n = nroot(a,b,c)

if disc(a,b,c) == 0:
    d = "1 real root, this is "
    print("This function has", d, p)
elif disc(a,b,c) > 0:
    d = "2 real roots, these are"
    print("This function has", d, p, "and", n)
else:
    d = "2 complex roots, these are"
    print("This function has", d, p, "and", n)
