# https://www.machinelearningplus.com/python/parallel-processing-python/

import multiprocessing as mp
import numpy as np
from time import time

# Prepare data
np.random.RandomState(100)
arr = np.random.randint(0, 10, size=[200000, 5])
data = arr.tolist()
data[:5]
