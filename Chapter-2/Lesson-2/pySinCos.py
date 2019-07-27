# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
from math import *

x = np.arange(-100,100)
y = x**2 + 3
y1 = 60*x+4
y2 = x

plt.plot(x, y, 
         x, y1, 
         x, y2)

plt.plot.show()
