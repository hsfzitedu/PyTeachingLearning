a1 = "10010101000101"

b1 = 127
b2 = 111

# print(eval(a1))

# print(~eval(a1))

c1 = "00"+bin(b1)[2:]
c2 = bin(b2)[2:]

print("{0:>20}".format(c1))
print("{0:>20}".format(c2))
print("{0:>20}".format(bin(int(c1,2)+int(c2,2))[2:]))


# a2 = 0b1101010100101
a2 = 0b1010
a3 = ~a2
print("{0:>40}".format(bin(a2)))
print("{0:>40}".format(bin(a3)))

print(bin(~0b1010))


print(bin(-1)[0])

