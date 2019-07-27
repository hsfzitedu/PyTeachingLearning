import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-100,100,1000)
y = np.sin(x)+1
z = np.cos(x **2) + 4

plt.plot(x,y)
plt.plot(x,z)

plt.xlim(-100,100)
plt.ylim(-2,2)

plt.show()
