def add(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1,n2):
    return n1 / n2

def mod(n1,n2):
    return n1 % n2

def exp(n1,n2):
    return n1 ** n2

print("Please select operation:\n"
      "1.Addition\n"
      "2.Subtraction\n"
      "3.Multiplcation\n"
      "4.Division\n"
      "5.Modulus\n"
      "6.Exponential\n")

op = int(input("Select Operation (1-6): "))

if op not in (1,2,3,4,5,6):
    print("Invalid response")
else:
    n1 = int(input("Enter First Number: "))
    n2 = int(input("Enter Second Number: "))
    
    if op == 1:
        print (n1, "+", n2, "=", add(n1,n2))
    elif op == 2:
        print (n1, "-", n2, "=", sub(n1,n2))
    elif op == 3:
        print (n1, "*", n2, "=", mult(n1,n2))
    elif op == 4 and n2 == 0:
        print ("This result is undefined")
    elif op == 4 and n2 != 0:
        print (n1, "/", n2, "=", div(n1,n2))
    elif op == 5:
        print (n1, "mod", n2, "=", mod(n1,n2))
    elif op == 6:
        print (n1, "^", n2, "=", exp(n1,n2))    