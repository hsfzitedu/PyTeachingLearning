def addBinary(a,b):
    a = int(a, 2)
    b = int(b, 2)
    return bin(a+b)[2:]


a1 = input("a=")
b1 = input("b=")

print(addBinary(a1,b1))
