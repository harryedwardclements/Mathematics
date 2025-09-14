i = 1
x = []

def mod(n1,n2):
    return n1 % n2

n = int(input("Select a positive integer: "))

if n < 0:
    print("Please input a POSITIVE INTEGER")
else:
    while i <= n:
        if mod(n,i) == 0:
            x.append(i)
            i += 1
        else:
            i += 1
    print(n, "has", len(x), "factors:", x)