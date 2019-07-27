import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,30,100)
# y = np.sin(x) + np.sin(2*x)
y = 2*np.sin(2*np.pi*50*x) + np.sin(2*np.pi*120*x)+4*np.sin(2*np.pi*200*x)

# plt.xlim(-10,10)
# plt.ylim(-3,3)

plt.xlim(0,30)
plt.ylim(-10,10)

plt.plot(x,y)


plt.show()
