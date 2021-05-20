from algorithms.pathfinding_test import PyPathfinding as PyPathfinding1
from algorithms.pathfinding import PyPathfinding as PyPathfinding2

from util.profiler import meanTime
from util.profiler import fileProfile

import matplotlib.pyplot as plt
import numpy as np
import time

size = 10_000
iterations = 10
    
# grid = [[0 for x in range(size)] for y in range(3)]
grid = np.zeros((3, size),dtype='int8')

args = (grid, (0, 1), (size-1, 1), True)
p1 = PyPathfinding1(*args)  
p2 = PyPathfinding2(*args)

print('Starting benchmark...')
meanTime(iterations)(p1.AStar)()
meanTime(iterations)(p2.AStar)()

quit()

top = 7000
step = 100
results = np.zeros(int(top//step)-1, dtype='float64')

for idx, size in enumerate(range(step, top, step)):
    grid = list(np.zeros((size, size), dtype='int8'))
    # grid = list(np.random.randint(0, 2, size=(size, size), dtype='int8'))
    pathfinder = Pcpp(grid, (0, 0), (size-1, size-1), True)


    start = time.time()
    a = pathfinder.AStar()
    end = time.time()

    results[idx] = end-start

print(results)

plt.plot(range(step, top, step), results)
plt.show()
