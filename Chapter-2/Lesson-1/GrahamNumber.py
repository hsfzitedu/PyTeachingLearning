N = 3

# 两个箭头
gn2 = N ** N ** N
print(gn2)

# 三个箭头
gn3 = gn2 ** N
print(gn3)

# 四个箭头
gn4 = gn3 ** N
print("{0:.2e}".format(gn4))

# 五个箭头
gn5 = gn4 ** N
print("{0:,}".format(gn5))

