import matplotlib.pyplot as plt 
import random as rnd
import numpy as np

p1, p2 = np.random.randint(-30, 30, size=(2,2))

plt.xlim((-30,30))
plt.ylim((-30,30))
plt.xlabel('X axis')
plt.ylabel('Y axis')
x0, y0 = 0, 0

plt.plot(p1, p2, color="r")

plt.show()

'''
fig = plt.figure()


plt.show()
'''
