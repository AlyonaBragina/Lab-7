import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
from time import perf_counter
res = []
a2 = []
a1 = []

t1_start = perf_counter() 

for i in range(10**6+1):
    res.append(random.random() * random.random())

t1_stop = perf_counter()

t2_start = perf_counter()

for i in range(10**6+1):
    a1.append(random.random())

for i in range(10**6+1):
    a2.append(random.random())
a1 = np.array(a1)
a2 = np.array(a2)

np.multiply(a1, a2)

t2_stop = perf_counter()

print("Time 1 program:", t1_stop-t1_start)
print("Time 2 program:", t2_stop-t2_start)