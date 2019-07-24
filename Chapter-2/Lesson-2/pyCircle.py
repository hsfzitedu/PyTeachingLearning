import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle

fig = plt.figure() 
ax = fig.add_subplot(111)

c1 = plt.Circle(xy=(0.0,0.0), radius=2, alpha=0.5)

ax.add_patch(c1)

x,y = 0,0
ax.plot(x,y, "ro")

plt.axis("scaled")
plt.axis("equal")
plt.show()
