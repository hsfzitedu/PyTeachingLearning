


print(chr(65))
print(chr(66))
print(chr(67))


for i in range(65,256):
    print(chr(i))

for i in range(65,256):
    print("{0:<4}{1:^4}{2:>20}{3:>10}".format(chr(i), i, bin(i), hex(i)))
